# -*- coding: utf-8 -*-
import thulac
import os
import csv

from Model.neo_models import Neo4j

# 使用读取的文件内容作为user_dict参数调用thulac.thulac函数
pre_load_thu = thulac.thulac(user_dict=r'E:\graduation_project\kg_graph\backEnd\toolkit\dict.txt')  # 默认模式
print('thulac open!')

neo_con = Neo4j()  # 预加载neo4j
neo_con.connectDB()
print('neo4j connected!')

predict_labels = {}  # 预加载实体到标注的映射字典
filePath = os.getcwd()
with open(r'E:\graduation_project\kg_graph\backEnd\toolkit\predict_labels.txt', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        predict_labels[str(row[0])] = int(row[1])
print('predicted labels load over!')
