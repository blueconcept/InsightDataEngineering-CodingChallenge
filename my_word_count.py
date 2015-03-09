from __future__ import print_function
from multiprocessing import Pool
from collections import Counter
import sys
import os

class WordCountWriter():
    '''
    Counts the words of all text files in a directory in parallel with Pool
    '''

    def __init__(self, directory="wc_input"):
        '''
        INPUT: String
        OUTPUT: None
        Initializes WordCountWriter by getting the file names in the directory 
        '''
        self.file_names = [directory+'/'+file for file in os.listdir(directory) if file.endswith(".txt")]
        self.file_names.sort()

    def write_word_count(self, output_file="wc_output/wc_result.txt"):
        '''
        INPUT: String
        OUTPUT: None
        Counts the words from the list of files in the directory
        '''
        if self.file_names != None:
            p = Pool(3*len(output_file))
            combined_counter = self.combine_dict(p.map(word_count, self.file_names))
            self.write_dict(combined_counter, output_file)

    def combine_dict(self, counter_list):
        '''
        INPUT: List
        OUTPUT: Counter
        Takes all of the results of the pool and aggregates them into one Counter
        '''
        main_counter = counter_list[0]
        for i in xrange(1,len(counter_list)):
            main_counter = self.merge(main_counter, counter_list[i])
        return main_counter

    def merge(self, main_counter, counter):
        '''
        INPUT: Counter, Counter
        OUTPUT: Counter
        Combines the two counters
        '''
        for word,count in counter.iteritems():
            if word in main_counter:
                main_counter[word] += count
            else:
                main_counter[word] = count
        return main_counter

    def write_dict(self, counter, output_file_name):
        '''
        INPUT: Counter, String
        OUTPUT: None
        Writes the word count from the Counter to the output file
        '''
        f = open(output_file_name, 'w')
        lst = counter.items()
        lst.sort()
        for word, count in lst:
            if len(word) > 0:
                f.write(word+"\t"+str(count)+'\n')
        f.close()

def word_count(file_name):
    '''
    INPUT: String
    OUTPUT: None
    Function to be used for Pool, calls class to handle the word counting of a file
    '''
    wc = WordCounter(file_name)
    return wc.get_word_count()

class WordCounter():
    '''
    Class for word counting one file.

    '''
    
    def __init__(self, file_name):
        '''
        INPUT: String
        OUTPUT: None
        Initializes WordCounter with the text_file and the characters to be stripped
        '''
        self.text_file = open(file_name, 'r')
        self.stripped = ",.?';()[]:!$%*-_+={}|\/<>&^$#@`~ "+'"'
    
    def get_word_count(self):
        '''
        INPUT: None
        OUTPUT: Counter
        Counts words through initialized counter
        '''
        c = Counter()
        for line in self.text_file:
            for word in line.split():
                c.update([self.clean(word)])
        return c
    
    def clean(self, word):
        '''
        INPUT: None
        OUTPUT: None
        Cleans the word before it is counted
        '''
        word = word.replace('-','')
        return word.strip(self.stripped).lower()

if __name__ == '__main__':
    mw = WordCountWriter()
    mw.write_word_count() 