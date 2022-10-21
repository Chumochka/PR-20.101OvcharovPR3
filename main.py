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
def file_analysis():
    max_length=0
    min_length=10
    glas_char=0
    sogl_char=0
    one_char, two_char,three_char,four_char,five_char,six_char,seven_char,eight_char,nine_char,ten_char=0,0,0,0,0,0,0,0,0,0
    with open(str(os.getpid()),'r') as conn:
        str1=conn.readline().lower()
        while(str1!=''):
            if(min_length>len(str1)-1):
                min_length=len(str1)-1
            if(max_length<len(str1)-1):
                max_length=len(str1)-1
            if(len(str1)-1==1):
                one_char+=1
            elif(len(str1)-1==2):
                two_char+=1
            elif(len(str1)-1==3):
                three_char+=1
            elif(len(str1)-1==4):
                four_char+=1
            elif(len(str1)-1==5):
                five_char+=1
            elif(len(str1)-1==6):
                six_char+=1
            elif(len(str1)-1==7):
                seven_char+=1
            elif(len(str1)-1==8):
                eight_char+=1
            elif(len(str1)-1==9):
                nine_char+=1
            elif(len(str1)-1==10):
                ten_char+=1
            for i in str1.lower():
                if(i in glas):
                    glas_char+=1
                else:
                    sogl_char+=1
            str1=conn.readline().lower()
    print("*********************************************\nАналитика для файла " + str(os.getpid())+"\n*********************************************")
    print("1. Всего символов --> "+ str(glas_char+sogl_char))
    print("2. Максимальная длина слова --> "+str(max_length))
    print("3. Минимальная длина слова --> "+str(min_length))
    print("4. Средняя длина слова --> "+str(round((glas_char+sogl_char)/(one_char+two_char+three_char+four_char+five_char+six_char+seven_char+eight_char+nine_char+ten_char))))
    print("5. Количество гласных --> "+str(glas_char))
    print("6. Количество согласных --> "+str(sogl_char))
    print("7. Количество повторений слов с одинаковой длиной:\n")
    print("\t*1 сим. >> "+str(one_char))
    print("\t*2 сим. >> "+str(two_char))
    print("\t*3 сим. >> "+str(three_char))
    print("\t*4 сим. >> "+str(four_char))
    print("\t*5 сим. >> "+str(five_char))
    print("\t*6 сим. >> "+str(six_char))
    print("\t*7 сим. >> "+str(seven_char))
    print("\t*8 сим. >> "+str(eight_char))
    print("\t*9 сим. >> "+str(nine_char))
    print("\t*10 сим. >> "+str(ten_char))
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
