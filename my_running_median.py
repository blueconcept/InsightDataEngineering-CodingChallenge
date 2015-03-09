from __future__ import print_function
from multiprocessing import Pool
from median_heap import Median_Heap
import sys
import os

class MedianWriter():
    '''
    Class to write the running median
    '''

    def __init__(self, directory="wc_input"):
        '''
        INPUT: None
        OUTPUT: None
        Initializes the MedianWriter with the file_names for the files in the directory
        '''
        self.file_names = [directory+'/'+file for file in os.listdir(directory) if file.endswith(".txt")]
        self.file_names.sort()

    def write_median(self, output_file="wc_output/med_result.txt"):
        '''
        INPUT: String
        OUTPUT: None
        Writes the running median
        '''
        if self.file_names != None:
            p = Pool(3*len(output_file))
            median_list = p.map(word_count_line, self.file_names)
            f = open(output_file, 'w')
            med_heap = Median_Heap()
            for lst in median_list:
                for num in lst:
                    med_heap.push(num)
                    f.write(str(med_heap.formated_root()) + '\n')

def word_count_line(file_name):
    '''
    INPUT: None
    OUTPUT: List
    Counts the number of lines for a file, to be used for Pool
    '''
    f = open(file_name)
    word_count_list = []
    for line in f:
        word_count_list.append(len(line.split()))
    return word_count_list

if __name__ == '__main__':
    mw = MedianWriter()
    mw.write_median()