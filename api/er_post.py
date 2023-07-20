# -*- coding: utf-8 -*-
from toolkit.pre_load import pre_load_thu
from toolkit.NER import get_NE, temporaryok, get_explain, get_detail_explain


def get_er_res(text):
    ctx = []  # 存储返回的文本
    thu1 = pre_load_thu  # 提前加载好了

    # 使用thulac进行分词 TagList[i][0]代表第i个词
    # TagList[i][1]代表第i个词的词性

    text = text.strip()
    print('text', text)

    TagList = thu1.cut(text, text=False)

    NE_List = get_NE(text)  # 获取实体列表

    for pair in NE_List:  # 根据实体列表，显示各个实体
        text = {}
        if pair[1] == 0:
            continue
        if temporaryok(pair[1]):
            text['name'] = pair[0]
            text['explain'] = get_explain(pair[1])
            text['detailExplain'] = get_detail_explain(pair[1])
            continue

        text['name'] = pair[0]
        text['explain'] = get_explain(pair[1])
        text['detailExplain'] = get_detail_explain(pair[1])
        text['url'] = 'https://baike.baidu.com/item/' + pair[0]
        ctx.append(text)

    # TODO：分词，先不做
    # seg_word = ""
    # length = len(TagList)
    # for t in TagList:  # 测试打印词性序列
    #     seg_word += t[0] + " <strong><small>[" + t[1] + "]</small></strong> "
    # seg_word += ""
    # ctx['seg_word'] = seg_word

    return ctx


if __name__ == '__main__':
    get_er_res('原子弹是一种核武器，也称为原子核武器，是利用核裂变或核聚变反应释放巨大能量的武器。'
               '它是20世纪40年代中期研发出来的，是第二次世界大战期间最具破坏力的武器之一。'
               '原子弹的核心是裂变核材料（如铀或钚），通过将裂变材料聚集到一定程度并加以引爆，可以释放出巨大的能量和强大的冲击波。')
