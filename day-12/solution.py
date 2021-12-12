from collections import defaultdict


def get_adj(x):
    adj = defaultdict(set)
    for start, end in x:
        adj[start].add(end)
        adj[end].add(start)
    return adj


def dfs(node, adj, path, paths):
    if node == "end":
        path.append(node)
        paths.append(path)
    elif node.isupper():
        path.append(node)
        for next in adj[node]:
            dfs(next, adj, list(path), paths)
    elif node.islower():
        if node in path:
            return
        path.append(node)
        for next in adj[node]:
            dfs(next, adj, list(path), paths)
    return paths


def solution(adj):
    """Question 1"""
    paths = dfs("start", adj, [], [])
    # for p in paths:
    #     print(",".join(p))
    return len(paths)


def dfs2(node, adj, path, paths):
    if node == "end":
        path.append(node)
        paths.append(path)
    elif node.isupper():
        path.append(node)
        for next in adj[node]:
            if next != "start":
                dfs2(next, adj, list(path), paths)
    elif node.islower():
        # count how many times each small cave has been visited in this path
        if "start" in path:
            small_caves = list(filter(lambda n: n.islower(), path))

            small_caves.remove("start")
            count = defaultdict(int)
            for n in small_caves:
                count[n] += 1

            two_counts = []
            for n in count:
                if count[n] == 2:
                    two_counts.append(n)
            # print(two_counts)
            if len(two_counts) == 1 and path.count(node) >= 1:
                return
            else:
                pass

        path.append(node)
        for next in adj[node]:
            if next != "start":
                dfs2(next, adj, list(path), paths)
    return paths


def solution2(adj):
    """Question 2"""
    paths = dfs2("start", adj, [], [])
    # for p in paths:
    #     print(",".join(p))
    return len(paths)


def parse_input():
    f = open("input.txt", "r").read().split("\n")
    res = []
    for line in f:
        a, b = line.split("-")
        res.append([a, b])
    return res


if __name__ == "__main__":
    x = parse_input()

    adj = get_adj(x)

    print("Question 1 solution: \n", solution(adj))

    print("Question 2 solution: \n", solution2(adj))
