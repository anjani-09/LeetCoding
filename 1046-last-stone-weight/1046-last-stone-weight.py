class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        self.maxHeap = [-1 * stone for stone in stones]
        heapq.heapify(self.maxHeap)
        
        while len(self.maxHeap) > 1:
            y,x = heapq.heappop(self.maxHeap), heapq.heappop(self.maxHeap)
            
            if x==y:
                continue
            else:
                newStone = (y*-1) - (x*-1)
                heapq.heappush(self.maxHeap, (newStone*-1))
        if not self.maxHeap:
            return 0
        return self.maxHeap[0]*-1