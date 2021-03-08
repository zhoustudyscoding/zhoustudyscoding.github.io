# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:42:32 2020

@author: 14590
csv文件存入mongodb
"""
# 导包
from pymongo import MongoClient
import csv
# 创建连接MongoDB数据库函数
def connection():
    # 1:连接本地MongoDB数据库服务
    conn=MongoClient("localhost")
    # 2:连接本地数据库(yolanda)。没有时会自动创建
    db=conn.yolanda
    # 3:创建集合
    set1=db.base
    set2=db.money
    set3=db.knowledge
    set4=db.year
    # 4:看情况是否选择清空(两种清空方式，第一种不行的情况下，选择第二种)
    #第一种直接remove
    set1.remove(None)
    set2.remove(None)
    set3.remove(None)
    set4.remove(None)
    #第二种 remove不好用的时候
    # set1.delete_many({})
    return set1,set2,set3,set4

def insertToMongoDB1(set1):
    # 打开文件base_train_sum.csv
    with open('data\\base_train_sum.csv','r',encoding='gbk')as csvfile:
        # 调用csv中的DictReader函数直接获取数据为字典形式
        reader=csv.DictReader(csvfile)
        # 创建一个counts计数一下 看自己一共添加了了多少条数据
        counts=0
        for each in reader:
            # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
            if each['注册时间']=='NA':
                each['注册时间'] = -1 
            else:
                each['注册时间']=int(each['注册时间'])
            if each['注册资本']=='NA':
                each['注册资本'] = -1 
            else:
                each['注册资本']=int(each['注册资本'])
            each['行业']=str(each['行业'])
            each['区域']=str(each['区域'])
            each['企业类型']=str(each['企业类型'])
            each['控制人类型']=str(each['控制人类型'])
            if each['控制人持股比例']=='NA':
                each['控制人持股比例'] = -1 
            else:
                each['控制人持股比例']=float(each['控制人持股比例'])
                
            if each['flag']=='NA':
                each['flag'] = -1
            else:
                each['flag']=int(each['flag'])
                
            set1.insert(each)
            counts+=1
            print('成功添加了'+str(counts)+'条数据 ')
            
def insertToMongoDB2(set2):
 # 打开文件money_report_train_sum.csv
    with open('data\\money_report_train_sum.csv','r',encoding='gbk')as csvfile:
        # 调用csv中的DictReader函数直接获取数据为字典形式
        reader=csv.DictReader(csvfile)
        # 创建一个counts计数一下 看自己一共添加了了多少条数据
        counts=0
        for each in reader:
            # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
            if each['year']=='NA':
                each['year'] = -1 
            else:
                each['year']=int(each['year'])
            
            if each['债权融资额度']=='NA':
                each['债权融资额度'] = -1 
            else:
                each['债权融资额度']=float(each['债权融资额度'])
            if each['债权融资成本']=='NA':
                each['债权融资成本'] = -1 
            else:
                each['债权融资成本']=float(each['债权融资成本'])    
           
            if each['股权融资额度']=='NA':
                each['股权融资额度'] = -1 
            else:
                each['股权融资额度']=float(each['股权融资额度'])
            if each['股权融资成本']=='NA':
                each['股权融资成本'] = -1 
            else:
                each['股权融资成本']=float(each['股权融资成本'])
            
            if each['内部融资和贸易融资额度']=='NA':
                each['内部融资和贸易融资额度'] = -1 
            else:
                each['内部融资和贸易融资额度']=float(each['内部融资和贸易融资额度'])
            if each['内部融资和贸易融资成本']=='NA':
                each['内部融资和贸易融资成本'] = -1 
            else:
                each['内部融资和贸易融资成本']=float(each['内部融资和贸易融资成本'])
            
            if each['项目融资和政策融资额度']=='NA':
                each['项目融资和政策融资额度'] = -1 
            else:
                each['项目融资和政策融资额度']=float(each['项目融资和政策融资额度'])
            if each['项目融资和政策融资成本']=='NA':
                each['项目融资和政策融资成本'] = -1 
            else:
                each['项目融资和政策融资成本']=float(each['项目融资和政策融资成本'])
            
            set2.insert(each)
            counts+=1
            print('成功添加了'+str(counts)+'条数据 ')

def insertToMongoDB3(set3):  
# 打开文件knowledge_train_sum.csv
    with open('data\\knowledge_train_sum.csv','r',encoding='gbk')as csvfile:
        # 调用csv中的DictReader函数直接获取数据为字典形式
        reader=csv.DictReader(csvfile)
        # 创建一个counts计数一下 看自己一共添加了了多少条数据
        counts=0
        for each in reader:
            # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
    
            if each['专利']=='NA':
                each['专利'] = -1 
            else:
                each['专利']=int(each['专利'])
                
            if each['商标']=='NA':
                each['商标'] = -1 
            else:
                each['商标']=int(each['商标'])    
           
            if each['著作权']=='NA':
                each['著作权'] = -1 
            else:
                each['著作权']=int(each['著作权'])
            
            set3.insert(each)
            counts+=1
            print('成功添加了'+str(counts)+'条数据 ')

def insertToMongoDB4(set4):          
# 打开文件year_report_train_sum.csv
    with open('data\\year_report_train_sum.csv','r',encoding='gbk')as csvfile:
        # 调用csv中的DictReader函数直接获取数据为字典形式
        reader=csv.DictReader(csvfile)
        # 创建一个counts计数一下 看自己一共添加了了多少条数据
        counts=0
        for each in reader:
            # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
            if each['year']=='NA':
                each['year'] = -1 
            else:
                each['year']=int(each['year'])
            
            if each['从业人数']=='NA':
                each['从业人数'] = -1 
            else:
                each['从业人数']=int(each['从业人数'])
                
            if each['资产总额']=='NA':
                each['资产总额'] = -1 
            else:
                each['资产总额']=float(each['资产总额'])    
           
            if each['负债总额']=='NA':
                each['负债总额'] = -1 
            else:
                each['负债总额']=float(each['负债总额'])
           
            if each['营业总收入']=='NA':
                each['营业总收入'] = -1 
            else:
                each['营业总收入']=float(each['营业总收入'])
            
            if each['主营业务收入']=='NA':
                each['主营业务收入'] = -1 
            else:
                each['主营业务收入']=float(each['主营业务收入'])
           
            if each['利润总额']=='NA':
                each['利润总额'] = -1 
            else:
                each['利润总额']=float(each['利润总额'])
            
            each['净利润']=str(each['净利润'])
            
            if each['纳税总额']=='NA':
                each['纳税总额'] = -1 
            else:
                each['纳税总额']=float(each['纳税总额'])
            
            each['所有者权益合计']=str(each['所有者权益合计'])
            
            #利用公式：资产总额=负债总额+所有者权益合计
            if (each['资产总额']==-1) and (each ['负债总额']!=-1) and (each['所有者权益合计']!='NA') :
                each['资产总额'] = each['负债总额'] + eval(each['所有者权益合计'])  
            
            if each['负债总额']==-1 and each ['资产总额']!=-1 and each['所有者权益合计']!='NA':
                each['负债总额'] = each['资产总额'] - eval(each['所有者权益合计'])    
            
            if each['所有者权益合计']=='NA' and each['资产总额']!=-1 and each['负债总额']!=-1:
                each['所有者权益合计'] = str(each['资产总额'] - each['负债总额']) 
           
            set4.insert(each)
            counts+=1
            print('成功添加了'+str(counts)+'条数据 ')
    
    # 创建主函数
def main():
    set1,set2,set3,set4=connection()
    insertToMongoDB1(set1)
    insertToMongoDB2(set2)
    insertToMongoDB3(set3)
    insertToMongoDB4(set4)
# 判断是不是调用的main函数。这样以后调用的时候就可以防止不会多次调用 或者函数调用错误
    
if __name__=='__main__':
    main()