while (S := input()):
    print(sum(i in "aeiouAEIOU" for i in S)) if S != '#' else exit()