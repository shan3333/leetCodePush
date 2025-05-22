class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [False for _ in range(numCourses)]
        graph = defaultdict(list)

        for cour, pre in prerequisites:
            graph[pre].append(cour)

        finished = []
        def dfs(pre):
            for course in graph[pre]:
                if not visited[course]:
                    visited[course] = True
                    if not dfs(course): 
                        return False
                elif course not in finished:
                    return False
            finished.append(pre)
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                visited[i] = True
                if not dfs(i): return []
        
        finished.reverse()
        return finished

