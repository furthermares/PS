import copy

def expand_lock(lock, N, M, size):
    expanded_lock = [[0 for i in range(size)] for _ in range(size)]
    for y in range(N):
        for x in range(N):
            expanded_lock[y + M - 1][x + M - 1] = lock[y][x]
    return expanded_lock

def rotate(key):
    return [list(reversed(i)) for i in zip(*key)]

def is_unlock(y, x, key, lock, N, M):
    _lock = copy.deepcopy(lock)
    for _y in range(M):
        for _x in range(M):
            _lock[_y + y][_x + x] += key[_y][_x]

    for _y in range(N):
        for _x in range(N):
            if _lock[_y + M - 1][_x + M - 1] != 1:
                return False
    
    return True

def solution(key, lock):
    N = len(lock)
    M = len(key)
    size = (N - 1) * 2 + M
    expanded_lock = expand_lock(lock, N, M, size)
    
    for _ in range(4):
        for y in range(size - M + 1):
            for x in range(size - M + 1):
                if is_unlock(y, x, key, expanded_lock, N, M):
                    return True
        key = rotate(key)
    
    return False