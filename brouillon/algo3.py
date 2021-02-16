def plus_grande_sequence_wikipedia(E):
    P = [-1 for _ in E]
    M = [-1 for _ in E]

    L = 0
    for i in range(0, len(E)):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if E[M[mid]] < E[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]

        if newL > L:
            M[newL] = i
            L = newL
        elif E[i] < E[M[newL]]:
            M[newL] = i

    S = [-1 for i in range(L)]
    k = M[L]
    for i in range(L-1, -1, -1) :
        S[i] = k
        k = P[k]

    return S

E = [10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 1, 15, 6, 11, 0, 14, 7, 9]
b = plus_grande_sequence_wikipedia(E)
print("plus grande sequence ")
print([ E[i] for i in b ])
