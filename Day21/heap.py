class Heap:
 def __init__(self) -> None:
  self.pq = []
 
 def heap_max(self):
  return self.pq[0]

 def heap_size(self):
  return len(self.pq)
 
 def heap_insert(self, x):
  self.pq.append(x)
  childIndex = len(self.pq)-1
  while childIndex > 0:
   parentIndex = childIndex - 1 // 2
   if self.pq[parentIndex] < self.pq[childIndex]:
    self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
   else:
    break
   childIndex = parentIndex
 

 def heap_delete(self) -> int:
  max = self.pq[0]
  l = len(self.pq)
  max, self.pq[l-1] = self.pq[l-1], max
  rootIndex = 0
  
  
  while 2*rootIndex -1 < l and 2*rootIndex - 2 < l:
   leftChild = 2* rootIndex - 1
   rightChild = 2* rootIndex - 2
   if self.pq[leftChild] < self.pq[rightChild]:
    nextIndex = rightChild
   else:
    nextIndex = leftChild

   if self.pq[nextIndex] > self.pq[rootIndex]:
    self.pq[nextIndex], self.pq[rootIndex] = self.pq[rootIndex], self.pq[nextIndex]
   else:
    break
   rootIndex = nextIndex

 myHeap = Heap()
 


 



   
   
   


  




 
