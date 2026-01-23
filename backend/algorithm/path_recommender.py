from collections import defaultdict, deque

def recommend_learning_path(courses, prerequisites, learned_courses):
    """
    courses: dict {course_id: course_name}
    prerequisites: list of (course_id, pre_course_id)
    learned_courses: set of course_id
    """

    graph = defaultdict(list)
    indegree = defaultdict(int)

    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    queue = deque()
    for course in courses:
        if indegree[course] == 0 and course not in learned_courses:
            queue.append(course)

    path = []
    while queue:
        cur = queue.popleft()
        path.append(courses[cur])
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0 and nxt not in learned_courses:
                queue.append(nxt)

    return path

