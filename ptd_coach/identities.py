"""Synthetic identities only; selection is an explicit demo capability."""

USERS = {
    "student_demo_01": {"label": "Étudiant démo A", "role": "student", "team": "team_demo_01"},
    "student_demo_02": {"label": "Étudiant démo B", "role": "student", "team": "team_demo_01"},
    "student_demo_03": {"label": "Étudiant démo C", "role": "student", "team": "team_demo_02"},
    "tutor_demo_01": {"label": "Tuteur démo", "role": "tutor", "team": "team_demo_01"},
    "coordination_demo_01": {"label": "Coordination démo", "role": "coordination", "team": None},
    "admin_demo_01": {"label": "Administration démo", "role": "admin", "team": None},
}


def public_user(user_id):
    return dict(USERS[user_id], id=user_id)
