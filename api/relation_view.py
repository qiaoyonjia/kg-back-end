# -*- coding: utf-8 -*-
from toolkit.pre_load import neo_con
import json
import os

relationCountDict = {}
filePath = os.path.abspath(os.path.join(os.getcwd(), "."))
with open(r'E:\graduation_project\kg_graph\backEnd\toolkit\relationStaticResult.txt', "r", encoding='utf8') as fr:
    for line in fr:
        relationNameCount = line.split(",")
        relationName = relationNameCount[0][2:-1]
        relationCount = relationNameCount[1][1:-2]
        relationCountDict[relationName] = int(relationCount)


def sortDict(relationDict):
    for i in range(len(relationDict)):
        relationName = relationDict[i]['rel']['type']
        relationCount = relationCountDict.get(relationName)
        if (relationCount is None):
            relationCount = 0
        relationDict[i]['relationCount'] = relationCount

    relationDict = sorted(relationDict, key=lambda item: item['relationCount'], reverse=True)

    return relationDict


def get_er(text):
    entity = text
    db = neo_con
    entityRelation = db.getEntityRelationbyEntity(entity)
    if len(entityRelation) == 0:
        # ctx = {'name': '<h1>数据库中暂未添加该实体</h1>'}
        return []
    else:
        # 返回查询结果
        # 将查询结果按照"关系出现次数"的统计结果进行排序
        entityRelation = sortDict(entityRelation)
        return json.dumps(entityRelation, ensure_ascii=False)



if __name__ == '__main__':
    get_er('原子弹')
