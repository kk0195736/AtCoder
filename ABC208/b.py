P = int(input())

F = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
F.reverse()

answer = 0

for i in F:
    syo = P // i
    if syo > 0:
        P -= syo * i
        answer += syo

print(answer)