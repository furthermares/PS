def solution(brown, yellow):
    w = (brown + yellow) // 3
    h = 3
    
    while (w - 2) * (h - 2) != yellow:
        w -= 1
        h = (brown + yellow) // w
    
    return [w, h]