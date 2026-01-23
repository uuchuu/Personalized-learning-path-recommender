from collections import defaultdict, deque
from algorithm.graph_builder import build_graph

def recommend_learning_path(courses, prerequisites, learned_courses):
    graph = build_graph(prerequisites)
    indegree = defaultdict(int)

    for course, pre in prerequisites:
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

