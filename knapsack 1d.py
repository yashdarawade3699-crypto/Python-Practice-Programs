n, W = map(int, input().split())

weights = list(map(int, input().split()))
values = list(map(int, input().split()))

dp = [0] * (W + 1)

for i in range(n):
    for w in range(W, weights[i] - 1, -1):
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

print(dp[W])