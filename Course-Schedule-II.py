class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def find_graph(prerequisites):
            graph = defaultdict(list)
            for dest, src in prerequisites:
                graph[src].append(dest)
            return graph

        def find_indegree(graph):
            indegree = { i: 0 for i in range(numCourses) }
            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
            return indegree

        def topo_sort(graph):
            res = []
            q = deque()
            indegree = find_indegree(graph)
            for node in indegree:
                if indegree[node] == 0:
                    q.append(node)
            while len(q)>0:
                node = q.popleft()
                res.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
            return res if numCourses == len(res) else []

        return topo_sort(find_graph(prerequisites))