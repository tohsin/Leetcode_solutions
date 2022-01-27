
def findLongestChain() -> int:
        pairs=[[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
        pairs.sort()
        print(pairs)
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                print(pairs[i][1])
                print(pairs[j][0])
                print(i,j)
                if pairs[i][1] < pairs[j][0]:
                    print("true")
                    dp[j] = max(dp[j], dp[i] + 1)
                   
                    print(dp)
                else:
                    print("false")
        return max(dp)
findLongestChain()