class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        lo = 0
        hi = len(citations) - 1
        h = 0

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            n_papers_greater = len(citations) - mid

            if n_papers_greater <= citations[mid]:
                hi = mid - 1
                h = max(h, n_papers_greater)
            else:
                lo = mid + 1

        return h
