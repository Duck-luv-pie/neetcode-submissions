class Solution:
    def climbStairs(self, n: int) -> int:
        #we want the number of distinct ways to climb to the top of the staircase

        #we can have dp[i] be the number of ways we can climb to that given state
        #dp[i] can come from a 1 step or a 2 step
        #that means dp[i] = dp[i-1] + dp[i-2]

        #given this, we must find the smallest possible values:
        #dp[0], d[1] = 0 ways (cause you can't get there with either 1 or 2), and 1 way (cause you can only use 1 to get there)


        #the following is optimal in time but not in space.
        #assign smallest:
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]


        #this would be a both time efficient and space efficient solution:
        previous_1 = 1
        previous_2 = 1
        current = 1

        for i in range(2, n + 1):
            current = previous_1 + previous_2

            previous_1 = previous_2
            previous_2 = current
        
        return current
