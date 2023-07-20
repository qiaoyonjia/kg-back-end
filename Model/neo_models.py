from py2neo import Graph, Node, Relationship, cypher, Path
import neo4j


class Neo4j():
    graph = None

    def __init__(self):
        print("create neo4j class ...")

    def connectDB(self):
        self.graph = Graph("http://localhost:7474", user="neo4j", password="1998")

    def matchItembyTitle(self, value):

        sql = "MATCH (n:Item { title: '" + str(value) + "' }) return n;"
        answer = self.graph.run(sql).data()
        return answer


    def matchHudongItembyTitle(self, value):
        sql = "MATCH (n:核综合知识 { name: '" + str(value) + "' }) return n;"
        try:
            answer = self.graph.run(sql).data()
        except:
            print(sql)
        return answer


    def getEntityRelationbyEntity(self, value):
        answer = self.graph.run("MATCH (entity1) - [rel] -> (entity2)  WHERE entity1.name = \"" + str(
            value) + "\" RETURN rel,entity2").data()
        return answer

    def findRelationByEntity(self, entity1):
        answer = self.graph.run("MATCH (n1 {name:\"" + str(entity1) + "\"})- [rel] -> (n2) RETURN n1,rel,n2").data()
        return answer

    def findRelationByEntity2(self, entity1):
        answer = self.graph.run("MATCH (n1)- [rel] -> (n2 {name:\"" + str(entity1) + "\"}) RETURN n1,rel,n2").data()

        return answer

    def findOtherEntities(self, entity, relation):
        answer = self.graph.run("MATCH (n1 {name:\"" + str(entity) + "\"})- [rel {type:\"" + str(
            relation) + "\"}] -> (n2) RETURN n1,rel,n2").data()
        return answer


    def findOtherEntities2(self, entity, relation):
        answer = self.graph.run("MATCH (n1)<- [rel {type:\"" + str(relation) + "\"}] -> (n2 {name:\"" + str(
            entity) + "\"}) RETURN n1,rel,n2").data()
        return answer

    # 根据两个实体查询它们之间的最短路径
    def findRelationByEntities(self, entity1, entity2):
        print('entity11', entity1)
        print('entity22', entity2)
        answer = self.graph.run("MATCH (p1:核综合知识{name:\"" + str(entity1) + "\"}),(p2:核综合知识{name:\"" + str(
            entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN rel").evaluate()
        print('answer', answer)
        if (answer is None):
            answer = self.graph.run(
                "MATCH (p1:law {name:\"" + str(entity1) + "\"}),(p2:tiaoItem {name:\"" + str(
                    entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN p").evaluate()
        if (answer is None):
            answer = self.graph.run("MATCH (p1:NewNode {title:\"" + str(entity1) + "\"}),(p2:HudongItem{title:\"" + str(
                entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN p").evaluate()
        if (answer is None):
            answer = self.graph.run("MATCH (p1:NewNode {title:\"" + str(entity1) + "\"}),(p2:NewNode {title:\"" + str(
                entity2) + "\"}),p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN p").evaluate()
        relationDict = []
        if (answer is not None):
            for x in answer:
                tmp = {}
                start_node = x.start_node
                end_node = x.end_node
                tmp['n1'] = start_node
                tmp['n2'] = end_node
                tmp['rel'] = x
                relationDict.append(tmp)
        return relationDict


    # 查询数据库中是否有对应的实体-关系匹配
    def findEntityRelation(self, entity1, relation, entity2):
        answer = self.graph.run("MATCH (n1:核综合知识 {name:\"" + str(entity1) + "\"})<- [rel:RELATION {type:\"" + str(
            relation) + "\"}] -> (n2:核综合知识{name:\"" + str(entity2) + "\"}) RETURN n1,rel,n2").data()
        if (answer is None):
            answer = self.graph.run(
                "MATCH (n1:HudongItem {title:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
                    relation) + "\"}] -> (n2:NewNode{title:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()
        if (answer is None):
            answer = self.graph.run("MATCH (n1:NewNode {title:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
                relation) + "\"}] -> (n2:HudongItem{title:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()
        if (answer is None):
            answer = self.graph.run("MATCH (n1:NewNode {title:\"" + str(entity1) + "\"})- [rel:RELATION {type:\"" + str(
                relation) + "\"}] -> (n2:NewNode{title:\"" + entity2 + "\"}) RETURN n1,rel,n2").data()
        return answer

