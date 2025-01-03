def dijkstra(graph: list, src: str, dest: str) -> list:
    # 1. Create an empty set for unvisited nodes
    unvisited = set()

    # 2. Create empty dictionary for predecessors
    predecessors = {}

    # 3. Create empty dictionary for distances
    distances = {}

    # 4. Add each node to unvisited set (.add to sets, .append to lists)
    for node in graph:
        unvisited.add(node)

    # 5 & 6. Set distance to src as 0, all others as infinity
    for node in graph:
        if node == src:
            distances[node] = 0
        else:
            distances[node] = float('inf')

    # 7. Main algorithm loop
    while unvisited:
        # Get node with minimum distance that hasn't been visited
        min_dist_node = get_min_dist_node(distances, unvisited)

        # If we can't find a minimum distance node, break
        if min_dist_node is None:
            break

        # Remove the node from unvisited (mark as visited)
        unvisited.remove(min_dist_node)

        # If we've reached our destination, we're done
        if min_dist_node == dest:
            return get_path(dest, predecessors)

        # Check all neighbors of current node
        for neighbor, weight in graph[min_dist_node].items():
            if neighbor in unvisited:
                # Calculate total distance to neighbor through current node
                distance_through_min_node = distances[min_dist_node] + weight

                # If we found a shorter path, update it
                if distance_through_min_node < distances[neighbor]:
                    distances[neighbor] = distance_through_min_node
                    predecessors[neighbor] = min_dist_node

    # If we get here, there's no path to destination
    return None

def get_path(dest, predecessors):
    path = []
    pred = dest
    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred, None)
    path.reverse()
    return path


def get_min_dist_node(distances, unvisited):
    min_dist = float("inf")
    min_dist_node = None
    for v in unvisited:
        distance_so_far = distances[v]
        if distance_so_far < min_dist:
            min_dist = distance_so_far
            min_dist_node = v
    return min_dist_node
