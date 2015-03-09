from heap import Min_Heap
from heap import Max_Heap

class Median_Heap():
    '''
    Tracks the median by using a min and max heap
    Access is O(1)
    Insertion is O(log N)
    '''
    
    def __init__(self):
        '''
        INPUT: None
        OUTPUT: None
        Initializes Median_Heap with a min and max heap
        '''
        self.min_heap = Min_Heap()
        self.max_heap = Max_Heap()
        
    def push(self, item):
        '''
        INPUT: int/float
        OUTPUT: None
        Inserts item to the a specific heap
        '''
        #push into heap that it fits into, when between min and max, get to max arbitrarily
        if len(self.min_heap) == 0:
            self.min_heap.push(item)
        elif len(self.max_heap) == 0:
            self.max_heap.push(item)
        else:
            if self.min_heap.get_root() < item:
                self.min_heap.push(item)
            else:
                self.max_heap.push(item)
            self.balance()
        
    def balance(self):
        '''
        INPUT: None
        OUTPUT: None
        Makes sure heaps don't have a length difference of more then 1
        '''
        diff = len(self.max_heap) - len(self.min_heap)
        while(diff != 0 and diff != 1):
            if diff < 0:
                self.max_heap.push(self.min_heap.pop())
            elif diff > 1:
                self.min_heap.push(self.max_heap.pop())
            diff = len(self.max_heap) - len(self.min_heap)
            
    def get_root(self):
        '''
        INPUT: None
        OUTPUT: float
        Returns the median which comes from the average of the roots or root of the heap with more nodes
        '''
        if len(self.max_heap) == len(self.min_heap):
            return (float(self.max_heap.get_root())+float(self.min_heap.get_root()))/2
        elif len(self.max_heap) > len(self.min_heap):
            return float(self.max_heap.get_root())
        elif len(self.max_heap) < len(self.min_heap):
            return float(self.min_heap.get_root())

    def formated_root(self):
        '''
        INPUT: None
        OUTPUT: float
        Returns the median with a formating of 1 decimal place, done by truncation rather then rounding
        '''
        return float("%.1f" % self.get_root())