def compute_course_priority(course_difficulty, student_level, target):
    """
    Simple interpretable weight model
    """
    base = 10 - abs(course_difficulty - student_level)

    if target == "job":
        bonus = 2
    elif target == "research":
        bonus = 1
    else:
        bonus = 0

    return base + bonus
