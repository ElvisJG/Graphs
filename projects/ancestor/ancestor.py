from projects.ancestor.util import Graph, Queue


def earliest_ancestor(ancestors, starting_node):
    # Initialize empty graph
    graph = Graph()
    terminal_paths = []

    # Add nodes and edges to graph
    for pair in ancestors:
        for vertices in pair:
            # Add nodes if not already in vertices
            if vertices not in graph.vertices:
                graph.add_vertex(vertices)
        # Add unidirectional edge representing the "is a child of" relation
        graph.add_edge(pair[1], pair[0])

    # Create empty queue
    queue = Queue()
    # Add path from the starting node to the queue
    queue.enqueue([starting_node])
    # Create empty set
    visited = set()
    # While the queue is not empty
    while queue.size() > 0:
        # Dequeue the first path
        path = queue.dequeue()
        # Grab the last vertex from the path
        last_vertex = path[-1]
        # Check if it has parents
        if graph.get_neighbors(last_vertex) == set():
            # If not, append to list of terminal paths
            terminal_paths.append(path)
        # Check if node has been visited
        if last_vertex not in visited:
            # If not, mark it visited
            visited.add(last_vertex)
            # For each parent
            for neighbor in graph.get_neighbors(last_vertex):
                # Make a copy of the path before adding
                path_copy = path.copy()
                # Add the parent to the path
                path_copy.append(neighbor)
                # Add the appended path to the queue
                queue.enqueue(path_copy)

    # Find how long the longest path is in terminal_paths
    max_length = max(len(p) for p in terminal_paths)
    # Create a list of all paths that are of length max_length
    longest_paths = [p for p in terminal_paths if len(p) == max_length]

    # Return -1 if the starting node has no parents
    if max_length == 1:
        return -1
    # If there's a unique longest path, return the earliest ancestor from the end of it
    if len(longest_paths) == 1:
        return longest_paths[0][-1]
    # If there are multiple longest paths => the earliest ancestor with the lowest id number
    if len(longest_paths) > 1:
        candidates = [p[-1] for p in longest_paths]
        return min(candidates)
