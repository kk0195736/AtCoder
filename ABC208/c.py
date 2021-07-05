N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

d = 0

if N <= K:
    d = (K - N) // N + 1
    K -= N * d

answer = [d] * N

b = sorted(enumerate(a), key=lambda x: x[1])

for i in range(K):
    answer[b[i][0]] += 1

for i in answer:
    print(i)