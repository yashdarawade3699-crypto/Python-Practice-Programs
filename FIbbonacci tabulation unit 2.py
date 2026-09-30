n=int(input("Enter a number: "))

dp=[0]*n

if n>=1:
    dp[0]=0
if n>=2:
    dp[1]=1

for i in range(2,n):
    dp[i]=dp[i-1]+dp[i-2]
print(dp)
