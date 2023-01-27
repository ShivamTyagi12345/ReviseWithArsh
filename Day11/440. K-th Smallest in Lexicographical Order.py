class Solution:
    def findKthNumber(self, n: int, k: int) -> int:


        
        # heapify(heap)
        def insert(heap, x):
            heap.append(x)
            last = len(heap)-1
            while last > 0:
                parent = last - 1 // 2
                if heap[parent] < heap[last]:
                    heap[parent], heap[last] = heap[last], heap[parent]
                else:
                    break
                last = parent 
        
        def delete(heap):
            maximum = heap[0]
            start = 0
            l = len(heap)
            # swap 
            maximum, heap[l-1] = heap[l-1], maximum
            #delete
            heap = heap[0:l-1]
            #heapify
            while 2*start - 1 < l and 2*start - 2  < l:
                left = 2 * start -1
                right = 2* start - 2
                if heap[left] < heap[right]:
                    maxIndex = right
                else:
                    maxIndex = left
                
                if heap[maxIndex] < heap[start]:
                    heap[maxIndex], heap[start] = heap[start], heap[maxIndex]
                else:
                    break
        heap = []
        for num in range(1, n+1):
            # heappush(heap, str(-num))
            
            insert(heap, str(num))
            if len(heap) > k:
                delete(heap )
        print(heap)
        return int(heap[0])
        
        
        


            
        