class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        finished = []
        graph = defaultdict(list)

        for cour, pre in prerequisites:
            graph[pre].append(cour)
        
        visited = [False for _ in range(numCourses)]
        def dfs(cour):
            for pre in graph[cour]:
                if not visited[pre]:
                    visited[pre] = True
                    if not dfs(pre): 
                        return False
                elif pre not in finished:
                    return False

            finished.append(cour)
            return True

        for i in range(numCourses):
            if not visited[i]:
                visited[i] = True
                if not dfs(i):
                    return []
        
        finished.reverse()
        return finished