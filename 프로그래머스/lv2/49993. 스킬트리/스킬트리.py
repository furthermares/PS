def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        stack = list(skill)
        for j in i:
            if j in skill and j != stack.pop(0):
                break
        else:
            answer += 1

    return answer