import heapq

#거리 변수에 대한 초기화
distance = [INF] * (city+1)
#최단 거리 함수
def short_dis(start):
    q = []
    heapq.heappush(q, (0,1)) #앞의 값이 맨 앞에 위치하도록 (거리, 도시)
    distance[start] = 0
    # until q get empty
    while q:
        dist, now = heapq.heappop(q)
        #check wheter visited or not
        if distance[now] < dist:
            continue
        # cal distance to linked city and store
        for i in graph[now]: # (city,weight) i[0]:linked city, i[1]:weitght to city
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

short_dis(1)