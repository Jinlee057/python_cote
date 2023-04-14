#변수 정리
INF = float("inf") #for setting node
city = 6 # #of cities
road = 11 # #of road
start = 1 # start city

#지도구현 : 인접리스트 (파이썬의 리스트 자료형)
#도시시작은 1번, 인덱스번호와 매칭하기 위해 0번은 가상으로 비워둔다.
#idx from graph = city # , (linked city, weight)
graph = [[],
         [(2,2),(3,5),(4,1)],
         [(3,3),(4,2)],
         [(2,3),(6,5)],
         [(3,3),(5,1)],
         [(3,1),(6,2)],
         []
]

#거리와 Done, Todo 정리
distance = [INF] * (city+1)
visited = [False] * (city+1)


#function to check next city
# shortest city among unvisited

def get_smallest_node():
    min_value = INF
    min_index = 0
    
    #check each city
    for node in range(1, city+1):
        if (not visited[node]) & (distance[node] < min_value):
            min_value = distance[node]
            min_index = node
    return min_index

#function to check shortest : get start info. record shortest way into distance

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    
    #get  city inform from start point
    
    for j in graph[start]: #idx# = city# [(linked city, distance)]
        distance[j[0]] = j[1] #check rest of city
    for _ in range(city-1): #start city already cleared.
        #which one is shortes?
        now = get_smallest_node()
        visited [now] = True 
        #check distance about linked node
        for k in graph[now]: #k (city,dis)
            new_distance = distance[now] + k[1]
            # pick whichever shortest
            if new_distance < distance[k[0]]:
                distance[k[0]] = new_distance
            else:
                pass