from ast import Str
from typing import List
from multiprocessing import Process
import multiprocessing
import time
import os
import threading
import random
from RandomWordGenerator import RandomWord

rnd=RandomWord(max_word_size=10, constant_word_size=False)

glas=['a','e','i','o','u','y']
wordlength = []
def file_analysis():
    max_length=0
    min_length=10
    glas_char=0
    sogl_char=0
    with open(str(os.getpid()),'r') as conn:
        str1=conn.readline().lower()
        while(str1!=''):
            if(min_length>len(str1)-1):
                min_length=len(str1)-1
            if(max_length<len(str1)-1):
                max_length=len(str1)-1
            wordlength.append(len(str1)-1)
            for i in str1.lower():
                if(i in glas):
                    glas_char+=1
                else:
                    sogl_char+=1
            str1=conn.readline().lower()
    sum=0
    for i in range(1,11):
        sum += wordlength.count(i)
    print("*********************************************\nАналитика для файла " + str(os.getpid())+"\n*********************************************")
    print("1. Всего символов --> "+ str(glas_char+sogl_char))
    print("2. Максимальная длина слова --> "+str(max_length))
    print("3. Минимальная длина слова --> "+str(min_length))
    print("4. Средняя длина слова --> "+str(round((glas_char+sogl_char)/sum)))
    print("5. Количество гласных --> "+str(glas_char))
    print("6. Количество согласных --> "+str(sogl_char))
    print("7. Количество повторений слов с одинаковой длиной:\n")
    for i in range(1,11):
        print("\t*"+str(i)+" сим. >> "+str(wordlength.count(i)))
def file_fill():
    a=random.randint(1E5,5E6)
    with open(str(os.getpid()),'a') as conn:
        for i in range(a):
            conn.write(rnd.generate()+"\n")
    file_analysis()
list_process :List[Process] = []
if __name__ == '__main__':
    for i in range(4):
        p=Process(target=file_fill)
        p.start()
        list_process.append(p)
    [process.join() for process in list_process]
