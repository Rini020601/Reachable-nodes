def dfs(adj_list, start_node, visited):
    visited.add(start_node)
    for neighbor in adj_list[start_node]:
        if neighbor not in visited:
            dfs(adj_list, neighbor, visited)

def reachable(adj_list, start_node):
    visited = set()
    dfs(adj_list, start_node, visited)
    return visited


adj_list = [[1, 3], [2], [0], [4], [3], []]
print("Nodes that are reachable from 0:", reachable(adj_list, 0))  
print("Nodes that are reachable from 3:", reachable(adj_list, 3))  
