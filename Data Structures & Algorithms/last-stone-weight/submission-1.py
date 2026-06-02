class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones) > 1):
            x = max(stones)
            stones.remove(x)
            y = max(stones)
            stones.remove(y)
            if x == y:
                if len(stones) == 0:
                    return 0                
            elif x > y:
                x = (x-y)
                stones.append(x)
        return stones[0]