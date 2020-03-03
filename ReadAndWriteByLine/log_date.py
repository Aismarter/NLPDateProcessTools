import os
import re


with open("prod_devops.txt",mode = 'r',encoding= 'utf-8') as f1:
    with open("classify_date_log",mode = 'w',encoding= 'utf8') as f2:
     #   inside_txt = f1.read()
     #   string_list = inside_txt.split('),')  # 注意两个python中\\代表一个反斜杠
     #   for line in string_list:
     #       print(line)
        for line in f1:
            f2.write(line)
            print(line)

    #    print(20 * '****')
    #    for line in string_list:
    #        if '(' in line:
    #            print(line)
