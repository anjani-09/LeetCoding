class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for X,Y in points:
            distance = (X)*(X)+(Y)*(Y)
            heap.append([distance, X,Y])
        heapq.heapify(heap)
        while k:
            distance, X, Y = heapq.heappop(heap)
            res.append([X,Y])
            k-=1
        return res
        