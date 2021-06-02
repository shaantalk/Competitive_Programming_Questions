from heapq import heappop, heappush


def solution(allLocations, numOfDeliveries):
    heap = []

    for idx, location in enumerate(allLocations):
        heappush(heap, (location[0]**2 + location[1]**2, idx))

    res = []
    while numOfDeliveries != 0:
        res.append(allLocations[heappop(heap)[1]])
        numOfDeliveries -= 1
    return res


allLocations = [[5, 5], [1, 2], [1, -1], [3, 4]]
numOfDeliveries = 2

print(solution(allLocations, numOfDeliveries))
