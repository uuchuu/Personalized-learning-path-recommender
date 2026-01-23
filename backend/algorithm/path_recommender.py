from collections import defaultdict, deque

def recommend_learning_path(courses, prerequisites, learned_courses, target="AI"):
    """
    个性化学习路径推荐算法
    """

    graph = defaultdict(list)
    indegree = defaultdict(int)

    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    queue = deque()
    for c in courses:
        if indegree[c] == 0 and c not in learned_courses:
            queue.append(c)

    path = []

    while queue:
        cur = queue.popleft()

        # 个性化权重策略（示意）
        if target == "AI" and "Machine" in courses[cur]:
            path.insert(0, courses[cur])  # AI方向课程优先
        else:
            path.append(courses[cur])

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0 and nxt not in learned_courses:
                queue.append(nxt)

    return path
