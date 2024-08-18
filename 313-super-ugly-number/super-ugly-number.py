class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = {1}
        heap =  [1]
        ugly = 1
        for _ in range(n):
            ugly = heapq.heappop(heap)
            for factor in primes:
                new_ugly = ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return ugly
