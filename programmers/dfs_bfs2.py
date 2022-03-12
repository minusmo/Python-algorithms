
def solution(n, computers):
    networks = 0
    networks = get_networks(n, computers)
    return networks

def get_networks(n, computers):
    linkages = [[] for _ in range(n)]
    for index_of_computer in range(n):
        links = computers[index_of_computer]
        linkages[index_of_computer] = update_linkage(linkages[index_of_computer], links, n, index_of_computer)
    vertexes = [i for i in range(n)]
    networks = bf_search(vertexes, linkages)
    return networks

def update_linkage(linkage, links, n, index_of_computer):
    for i in range(n):
        if i == index_of_computer:
            continue
        else:
            if links[i] == 1:
                linkage.append(i)
            else:
                continue
    return linkage

def bf_search(vertexes, linkages):
    networks = 0
    visited = [] #queue
    need_visit = [] #queue
    not_visited = 0
    while not not_visited == None:
        need_visit.append(not_visited)
        find_linked_vertexes(need_visit, visited, vertexes, linkages)
        networks += 1
        not_visited = find_not_visited_vertex(vertexes)
    return networks

def find_not_visited_vertex(vertexes):
    if len(vertexes) > 0:
        return vertexes[0]
    else:
        return None

def find_linked_vertexes(need_visit, visited, vertexes, linkages):
    while len(need_visit) > 0:
        current_vertex = need_visit.pop(0)
        if not current_vertex in visited:
            visited.append(current_vertex)
            vertexes.remove(current_vertex)
            need_visit.extend(linkages[current_vertex])
