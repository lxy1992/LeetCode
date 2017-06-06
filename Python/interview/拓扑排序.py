# -*- coding: UTF-8 -*-
def indegree0(v, e):
    if not v:
        return None
    tmp = v[:]
    # print "tmp:" + format(tmp)
    """从tmp中删除所有作为入度的节点,tmp中留下了入度为0的点"""
    for i in e:
        if i[1] in tmp:
            # print "i[1]:" + format(i[1])
            tmp.remove(i[1])
        if not tmp:
            return -1
    """设定入度为0所在点的边为'toDel来删除'"""
    for t in tmp:
        for i in xrange(len(e)):
            # print "i:" + format(i)
            if t in e[i]:
                e[i] = 'toDel'
                # print "e[i]:" + format(e[i])
    if e:
        # 去除重复的'toDel'
        eset = set(e)
        # 删除'toDel'
        eset.remove('toDel')
        # 将set转换为list
        e[:] = list(eset)
    # 从点集V中去除没有入度的点
    if v:
        for t in tmp:
            v.remove(t)
    return tmp


def sorttop(v,e):
    result=[]
    while True:
        nodes = indegree0(v,e)
        # print "nodes:" + format(nodes)
        if nodes == None:
            break
        if nodes == -1:
            print('there\'s a circle')
            return None
        result.extend(nodes)
    return result

if __name__ == '__main__':
    v = ['a', 'b', 'c', 'd', 'e']
    e = [('a', 'b'), ('a', 'd'), ('b', 'c'), ('d', 'c'), ('d', 'e'), ('e', 'c')]
    res = sorttop(v,e)
    print(res)