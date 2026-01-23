from collections import defaultdict

def build_graph(prerequisites):
    graph = defaultdict(list)
    for course, pre in prerequisites:
        graph[pre].append(course)
    return graph
