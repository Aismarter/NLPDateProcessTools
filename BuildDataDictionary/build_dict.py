#encoding = 'utf-8'
import os
import nltk
import string
from collections import Counter
import numpy as np
import tensorflow.keras as kr

def read_file(filename):

    data_i = open(filename,'r',encoding= 'utf-8')
    print("type_data_i",type(data_i))
    file_data = data_i.read()
    print ('type_file_data：',type(file_data ))
    print ('len of file_data:',len(file_data) )
    return file_data


def main():
    content = read_file('all_log.txt').split(' ')
    wordList = nltk.word_tokenize(content)
    print(wordList)

if __name__ == '__main__':
    main()