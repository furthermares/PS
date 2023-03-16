def solution(tickets):
    routes = {}
    for i in tickets:
        routes[i[0]] = routes.get(i[0], []) + [i[1]]
    for i in routes:
        routes[i].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or not routes[top]:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]