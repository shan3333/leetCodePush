1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        n = len(isConnected)
4        numOfProvince = 0
5        allCities = set([c for c in range(len(isConnected))])
6        checkedCities = set()
7        connectedCities = {0}
8        while len(checkedCities) < n:
9            while connectedCities:
10                city = connectedCities.pop()
11                for k, v in enumerate(isConnected[city]):
12                    if v == 1 and k is not city and k not in checkedCities:
13                        connectedCities.add(k)
14                checkedCities.add(city)
15            
16            numOfProvince += 1
17            uncheckedCities = allCities - checkedCities
18            if not uncheckedCities:
19                break
20            connectedCities = {uncheckedCities.pop()}
21
22        return numOfProvince