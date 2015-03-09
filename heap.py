import heapq

class Min_Heap():
    '''
    Data Structure for maintaining the smallest number at the root
    '''
    
    def __init__(self):
        '''
        INPUT: None
        OUTPUT: None
        Initializes Min_Heap
        '''
        self.lst = []
        
    def push(self, item):
        '''
        INPUT: int/float
        OUTPUT: None
        Adds the item to the heap
        '''
        heapq.heappush(self.lst,item)
    
    def get_root(self):
        '''
        INPUT: None
        OUTPUT: int/float
        Returns root of heap which is the min of the heap
        '''
        return self.lst[0]
    
    def print_heap(self):
        '''
        INPUT: None
        OUTPUT: None
        Prints the list
        '''
        print self.lst
        
    def pop(self):
        '''
        INPUT: None
        OUTPUT: int/float
        Return the removed root of the heap
        '''
        return heapq.heappop(self.lst)
        
    def __len__(self):
        '''
        INPUT: None
        OUTPUT: int
        Returns the length of the list
        '''
        return len(self.lst)
    
class Max_Heap(Min_Heap):
    '''
    Data Structure for maintaining the largest number at the root
    '''

    def __init__(self):
        '''
        INPUT: None
        OUTPUT: None
        Initializes the Max_Heap and calls super Min_Heap
        '''
        Min_Heap.__init__(self)
        
    def push(self, item):
        '''
        INPUT: int/float
        OUTPUT: None
        Adds the item and adjust for the Max_Heap
        '''
        out = heapq.heappush(self.lst,item*(-1))
        
    def get_root(self):
        '''
        INPUT: None
        OUTPUT: int/float
        Returns the root of the heap and adjust for the Max_Heap
        '''
        return self.lst[0]*(-1)

    def pop(self):
        '''
        INPUT: None
        OUTPUT: int/float
        Return the removed root of the heap and adjust for the Max_Heap
        '''
        return heapq.heappop(self.lst)*(-1)