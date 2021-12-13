from collections import defaultdict


def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        edge = edge.split('-')
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph


def solution(input_data):
    edges = input_data.strip().split('\n')
    cave_graph = build_graph(edges)
    number_of_paths = find_paths(cave_graph)
    return number_of_paths


def explore(node, graph, path, total_paths):
    if node.islower() and node in path:
        if path.count(node) > 1:
            return

        lower_case_caves_counts = [path.count(
            k) for k in graph.keys() if k.islower()]
        for count in lower_case_caves_counts:
            if count > 1:
                return

    path.append(node)

    if node == 'end':
        total_paths.append(tuple(path))
        return

    if node == 'start':
        return

    for neighbour in graph[node]:
        explore(neighbour, graph, path.copy(), total_paths)


def find_paths(cave_graph):
    start = cave_graph['start']
    path = ['start']
    total_paths = []
    for node in start:
        explore(node, cave_graph, path.copy(), total_paths)

    total_paths = set(total_paths)

    return len(total_paths)


if __name__ == '__main__':
    example1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

    print(solution(example1))

    example2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

    print(solution(example2))

    example3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

    print(solution(example3))

    with open('input.txt') as f:
        input_data = f.read()

    print(solution(input_data))
