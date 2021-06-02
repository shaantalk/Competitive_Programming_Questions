def demolitionBot(m):
    # Number of Rows and Columns
    R = len(m)
    C = len(m[0])

    # Starting row and column
    sr, sc = 0, 0

    # character to avoid while traversing
    character_not_to_visit = 0

    # character marking the goal location
    character_goal = 9

    # Row and Column queue
    rq = []
    cq = []

    # Variables used to track the numbers of steps taken
    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0

    # Variable used to track the E character
    reached_end = False

    # R*C matrix of False values used to track the node at position i,j is visited or Not
    visited = [[False for _ in range(R)] for _ in range(C)]

    # Direction vectors (North, South, East, West) :- Add more if diagonal moves are allowed
    dr = [-1, +1, 0, 0]
    dc = [0, 0, +1, -1]

    # visiting the start cell
    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True

    # Checking if rq is empty ( alternatively can also check cq )
    while len(rq) > 0:
        # Since the queues aren't empty, so we dequeue the current positions from rq and cq
        r = rq.pop(0)
        c = cq.pop(0)

        # If the bot reached the goal then break and mark that goal is reached
        if m[r][c] == character_goal:
            reached_end = True
            break

        # Otherwise we explore the neighbouring cells of the current position
        for i in range(len(dr)):
            # computing co-ordinates of a neighbour by adding one element from the direction vector to the current co-ordinates
            rr = r + dr[i]
            cc = c + dc[i]

            # Skip out of bounds locations
            if rr < 0 or cc < 0 or rr >= R or cc >= C:
                continue

            # Skip if the node is visited
            if visited[rr][cc] == True:
                continue

            # Skip if the node has the character not to visit
            if m[rr][cc] == character_not_to_visit:
                continue

            # Enqueue these co-ordinates to the rq and cq
            rq.append(rr)
            cq.append(cc)

            # Marking the neighbouring node as visited and adding one to the count of nodes in next layer
            visited[rr][cc] = True
            nodes_in_next_layer += 1

        # Everytime we complete one node we increment the number of steps taken i.e. the distance moved by the bot
        nodes_left_in_layer -= 1

        # Current layer's number of node reaches zero means this layer is over and since we chose only one next step from one layer so we increase the move_count
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    # if the flag is True then return the move_count else return -1 or False
    if reached_end:
        return move_count
    return -1


m = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 9, 1]
]

print(demolitionBot(m))
