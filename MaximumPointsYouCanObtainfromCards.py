class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lCards = len(cardPoints)
        runningTotal = sum(cardPoints[lCards-k::])
        curMax = runningTotal
        for i in range(k):
            runningTotal += (cardPoints[i] - cardPoints[lCards-k+i])
            curMax = max(curMax, runningTotal)
        return curMax
