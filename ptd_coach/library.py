"""Local, deterministic catalogue. Never reads conversations outside the supplied thread."""
import json
import math
import re
from collections import Counter
import unicodedata
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / 'pedagogy/library/methodes-v0.1.json'

def catalogue():
    return json.loads(PATH.read_text(encoding='utf-8'))['methodes']

def normalize(value):
    value = unicodedata.normalize('NFD', value.lower().replace('’', ' ').replace("'", ' '))
    return ''.join(c for c in value if not unicodedata.combining(c))

# Situations and weighted phrases are explicit and inspectable; not a skill classifier.
INTENTS = {
    'M01': ['rencontrer le client', 'voir le client', 'premier entretien', 'questions au client', 'comprendre sa demande'],
    'M02': ['besoin ou solution', 'vrai besoin', 'besoin du client', 'distinguer besoin'],
    'M03': ['cahier des charges', 'specifications', 'rediger le cahier', 'document de besoins'],
    'M04': ['exigence mesurable', 'exigence verifiable', 'critere acceptation', 'trop vague'],
    'M05': ['tracer les exigences', 'origine des exigences', 'verifier les exigences'],
    'M06': ['change d avis', 'change tout le temps', 'nouvelle demande', 'change regulierement', 'modifier le perimetre'],
    'M07': ['decouper les livrables', 'structure du projet', 'work breakdown', 'wbs'],
    'M08': ['prend du retard', 'projet en retard', 'dependance entre', 'date limite', 'faire un planning'],
    'M09': ['ne participe pas', 'ne contribuent pas', 'ne contribue pas', 'personne ne parle', 'retour experience', 'faire un bilan'],
    'M10': ['plusieurs causes', 'mesures varient', 'comprendre pourquoi', 'chercher les causes', 'resultats variables'],
}

# Normalize everyday expressions into a small concept vocabulary before comparing
# the query against authored example situations with TF-IDF cosine similarity.
# This is lexical retrieval, not semantic understanding or an LLM classifier.
CONCEPTS = {
    'commanditaire': ('commanditaire', 'client', 'cliente'),
    'changement': ('change', 'changer', 'changement', 'modifie', 'modifier', 'evolue'),
    'besoin': ('besoin', 'attente', 'demande', 'souhaite'),
    'retard': ('retard', 'delai', 'delais', 'echeance'),
    'planning': ('planning', 'calendrier', 'planifier', 'planification'),
    'exigence': ('exigence', 'exigences', 'critere', 'criteres', 'specification', 'specifications'),
    'equipe': ('equipe', 'groupe', 'membres', 'collectif'),
    'participer': ('participe', 'participent', 'contribue', 'contribuent', 'parle', 'parlent'),
    'cause': ('cause', 'causes', 'pourquoi', 'origine'),
}
STOP = set('le la les du des de un une et ou en au aux dans nous notre nos pour avec comment qui que est sont je vous mon ma mes faire'.split())
def tokens(value):
    words = re.findall(r'[a-z0-9]+', normalize(value))
    reverse = {word: concept for concept, variants in CONCEPTS.items() for word in variants}
    return [reverse.get(word, word) for word in words if len(word) > 2 and word not in STOP]

def similarity(query, examples):
    documents = [tokens(' '.join(INTENTS.get(item['id'], [])) + ' ' + item['nom']) for item in examples]
    counts = Counter(word for document in documents for word in set(document))
    q = Counter(tokens(query)); n = len(documents)
    def weight(word, count):
        return count * (1 + math.log((n + 1) / (1 + counts.get(word, 0))))
    qv = {word: weight(word, count) for word, count in q.items() if word in counts}
    qnorm = math.sqrt(sum(x*x for x in qv.values()))
    scores = {}
    for item, doc in zip(examples, documents):
        dv = {word: weight(word, count) for word, count in Counter(doc).items()}
        den = qnorm * math.sqrt(sum(x*x for x in dv.values()))
        scores[item['id']] = sum(qv.get(word, 0) * v for word, v in dv.items()) / den if den else 0
    return scores

def select(message, history=()):
    current = normalize(message)
    # Context is only used to resolve a short continuation after an earlier user turn.
    contextual = len(re.findall(r'\w+', current)) <= 7 and any(x in current for x in ('cela', 'ca', 'celle', 'ce cas', 'comment', 'et ensuite', 'exemple'))
    previous = next((normalize(x.get('content', '')) for x in reversed(history) if x.get('role') == 'user'), '') if contextual else ''
    text = current + (' ' + previous if previous else '')
    candidates = []
    items = catalogue()
    similarities = similarity(text, items)
    query_concepts = set(tokens(text))
    for item in items:
        phrases = [phrase for phrase in INTENTS.get(item['id'], []) if phrase in text]
        # Names are useful precise signals; loose keywords alone do not trigger coach injection.
        name_match = normalize(item['nom']) in text
        lexical = similarities[item['id']]
        # Require two distinct meaningful matching concepts for fallback; exact
        # authored situations may match directly. Abstain if evidence is weak.
        matching = query_concepts & set(tokens(' '.join(INTENTS.get(item['id'], [])) + ' ' + item['nom']))
        score = len(phrases) * 3 + (4 if name_match else 0) + lexical
        if phrases or name_match or (len(matching) >= 2 and lexical >= 0.23):
            candidates.append((score, item['id'], item, phrases))
    if not candidates:
        return None
    candidates.sort(key=lambda row: (-row[0], row[1]))
    score, _, item, phrases = candidates[0]
    return {'method': item, 'score': score, 'signals': phrases, 'context_used': bool(previous)}
