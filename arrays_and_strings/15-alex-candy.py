class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]

        for i in range(1, len(candies)):
            i0 = i + -1

            if ratings[i0] < ratings[i] and candies[i0] >= candies[i]:
                candies[i] = max(candies[i0] + 1, candies[i])

        for i in range(len(candies) - 1 - 1, -1, -1):
            i0 = i + 1

            if ratings[i0] < ratings[i] and candies[i0] >= candies[i]:
                candies[i] = max(candies[i0] + 1, candies[i])

        return sum(candies)
