  '''Tools.py
~~~~~~~~~~~~
    所有的工具函数存储包

~~~~~~~~~~~~
    使用手册：
    新增功能：日期变更问题
    两个日期变更函数均定义在Date类中，
        DateIncreases(self，filename)是来实现日期目前文件名中的日期自动增加一日
            使用方法：
                from Tools import *
                ...
                filename = Date().DateIncreases(filename)
            其中，filename通过这个函数后可以实现日期的一日增加
            例从'物料质量20171231.xlsx'到'物料质量20180101.xlsx'
        DateInteration(self,startfilename,endfilename)是来实现指定起始日期的遍历
            使用方法：
                from Tools import *
                ...
                Date().DateInteration(startfilename,endfilename)
            结果会输出从startfilename到endfilename的所有文件名

~~~~~~~~~~~~
    如在使用过程中发现bug请及时修复并更新至群中
'''

# -*- coding: utf-8 -*-
from math import *
class tongjl:
    def Average(self,x):    #计算平均值,其中去掉了空白值，计算的不是非空白区域的均值
        l = length = len(x)     #记录x的长度
        sum = 0
        for i in range(length):
            if(x[i] == ''):
                l = l - 1
            else:
                sum += x[i]
        if(l == 0):
            return 0
        return(sum/l)

    def Fangc(self,x):      #计算方差
        l = length = len(x)
        result = 0
        for i in range(length):
            if(x[i] == ''):
                l = l - 1
            else:
                index = x[i] - tongjl().Average(x)
                result += (index * index)
        if(l == 0):
            return 0
        return (result/l)
    def Biaozc(self,x):        #计算标准差
        y = tongjl().Fangc(x)
        '''result = []
        for i in range(len(y)):
            result.append(y[i] ** 0.5)
        '''
        return (y ** 0.5)
    def Zhongs(self,x):     #计算众数
        length = len(set(x))
        result = []
        index = max(x.count(i) for i in set(x))
        for s in set(x):
            if(x.count(s) == index):
                result.append(s)
        return result
    def Similarity(self,x,y):   #计算相似性
        result = 0
        return result
class date:
    def DateIteration(self,startfilename,endfilename):       #实现自动检索所有的日期
        while (startfilename != endfilename):
            startfilename = date.DateIncreases(self,startfilename)
            print(startfilename)
    def DateIncreases(self,filename):
        if (int(filename[filename.index(".") - 2:filename.index(".")]) < 9):
            filename = filename[:filename.index(".") - 1] + str(
                int(filename[filename.index(".") - 1]) + 1) + filename[filename.index("."):]
        elif (int(filename[filename.index(".") - 2:filename.index(".")]) < 28):
            filename = filename[:filename.index(".") - 2] + str(
                int(filename[filename.index(".") - 2:filename.index(".")]) + 1) + filename[filename.index("."):]
        elif (int(filename[filename.index(".") - 2:filename.index(".")]) == 28):
            if (int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 2):
                filename = filename[:filename.index(".") - 3] + str(
                    int(filename[filename.index(".") - 3]) + 1) + '01' + filename[filename.index("."):]
            else:
                filename = filename[:filename.index(".") - 2] + str(
                    int(filename[filename.index(".") - 2:filename.index(".")]) + 1) + filename[filename.index("."):]
        elif (int(filename[filename.index(".") - 2:filename.index(".")]) < 30):
            filename = filename[:filename.index(".") - 2] + str(
                int(filename[filename.index(".") - 2:filename.index(".")]) + 1) + filename[filename.index("."):]
        elif (int(filename[filename.index(".") - 2:filename.index(".")]) == 30):
            if (int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 4 or
                        int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 6):
                filename = filename[:filename.index(".") - 3] + str(
                    int(filename[filename.index(".") - 3]) + 1) + '01' + filename[filename.index("."):]
            elif (int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 9 or
                          int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 11):
                filename = filename[:filename.index(".") - 3] + str(
                    int(filename[filename.index(".") - 4:filename.index(".") - 2]) + 1) \
                           + '01' + filename[filename.index("."):]
            else:
                filename = filename[:filename.index(".") - 2] + str(
                    int(filename[filename.index(".") - 2:filename.index(".")]) + 1) + filename[filename.index("."):]
        elif (int(filename[filename.index(".") - 2:filename.index(".")]) == 31):
            if (int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 1 or
                        int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 3 or
                        int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 5 or
                        int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 7 or
                        int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 8):
                filename = filename[:filename.index(".") - 3] + str(
                    int(filename[filename.index(".") - 3]) + 1) + '01' + filename[filename.index("."):]
            elif (int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 10):
                filename = filename[:filename.index(".") - 4] + str(
                    int(filename[filename.index(".") - 4:filename.index(".") - 2]) + 1)+ '01' + filename[filename.index("."):]
            elif (int(filename[filename.index(".") - 4:filename.index(".") - 2]) == 12):
                filename = filename[:filename.index(".") - 6] + str(
                    int(filename[filename.index(".") - 6:filename.index(".") - 4]) + 1) + '0101' + filename[filename.index("."):]
        return filename