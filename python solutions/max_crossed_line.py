def maxUncrossedLines( nums1, nums2) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for i in range (n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                print(i ,j )
                print(nums1[i - 1] , nums2[j - 1])
                if nums1[i - 1] == nums2[j - 1]:
                    print(dp[i][j], dp[i - 1][j - 1] , nums1[i-1], nums2[j-1])
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[m][n]
maxUncrossedLines([10,5,2,1,5,2],
[2,5,1,2,5])