def permute(word):
    word = list(word)
    n = len(word)
    permutations = []
    permutations.append("".join(word))
    c = [0]*n
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                word[0], word[i] = word[i], word[0]
            else:
                word[c[i]], word[i] = word[i], word[c[i]]
            permutations.append("".join(word))
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    return permutations

word = input("Enter a word: ")
permutations = permute(word)
permutations