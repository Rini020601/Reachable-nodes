import unittest

def dfs(adj_list, start_node, visited):
    visited.add(start_node)
    for neighbor in adj_list[start_node]:
        if neighbor not in visited:
            dfs(adj_list, neighbor, visited)

def reachable(adj_list, start_node):
    visited = set()
    dfs(adj_list, start_node, visited)
    return visited

class TestReachable(unittest.TestCase):

    def test_reachable(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]

       
        reachable_from_0 = reachable(adj_list, 0)
        self.assertEqual(reachable_from_0, {0, 1, 2, 3, 4})

       
        reachable_from_3 = reachable(adj_list, 3)
        self.assertEqual(reachable_from_3, {3, 4})

if __name__ == '__main__':
    unittest.main()
