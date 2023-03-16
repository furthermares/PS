def solution(m, n, puddles):
    map = [[0] * (m + 1) for _ in range(n + 1)]
    map[1][1] = 1
    
    for x, y in puddles:
        map[y][x] = -1
        
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if map[y][x] == -1:
                map[y][x] = 0
                continue

            map[y][x] += (map[y][x - 1] + map[y - 1][x]) % 1000000007

    return map[n][m]