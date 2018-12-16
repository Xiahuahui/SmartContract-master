# -*- coding:utf-8 -*-
import pygraphviz as pgv
import numpy as np
M = np.zeros((1000,1000),dtype=np.str)
class Commitment:                        #定义承诺的结构
    def __init__(self, pre, res, tc):
        self.pre = pre
        self.res = res
        self.tc = tc
    def print_content(self):
        print(self.pre)
        print(self.res + ' ' + self.tc)
class St_node:                              # 定义了状态机中一个合理状态节点
   
    def __init__(self,Id,S):
        self.Id = Id               
        self.S = S
    def print_content(self):
        print(self.Id)
        print(self.S)
               
def create_state_transfers(commitments):   #生成状态机
    Repeat = []              # 重复列表
    Id = 0
    queue = []               #构造状态节点队列
    transfers = []           #构造状态转移队列            
    CC = commitments         #n个承诺的信息列表
    nums = len(CC)           # 承诺数量
    S = nums * [1]    # 初始状态 [1, 1, 1, ..., 1, 1]
    for i in range(len(CC)):               #初始下状态机的根节点
        connect = CC[i].pre[0]
        event = CC[i].pre[1]
        if connect == 0 and event == 0:
            S[i]=2
    st=St_node(Id,S)                  #初始化状态机的节点
    queue.append(st)                  #将初始状态放入队列
    Repeat.append(st)                 #将初始状态放入重复队列
    # 以bfs顺序建立图结构，图的每个结点是一个承诺状态列表
    while len(queue):
      
        st = queue.pop(0)            #状态节点出队
        (a,b,Id,Repeat) = createChildrenNodes(CC,st,Id,Repeat)  #遍历所有合理子状态
        queue.extend(a)                 #将所有的合理的子状态入队
        transfers.extend(b)             #将所有的状态转移入队
    return (transfers,Repeat)
def createChildrenNodes(commitments,st,Id,Repeat):#输入合理状态，返回所有子状态
    s = st.S                         #取出节点中状态
    queue = []                       #子节点的队列
    transfers = []                   #状态转移队列
    CC = commitments
    for i in range(len(s)):
        c_stat = s[i]                  #查看第i个承诺的状态，只有状态为1,2时才能转变
        if c_stat == 1:       #当该承诺状态为1时
            connect = CC[i].pre[0]       #取出该承诺的前提
            event = CC[i].pre[1]
            if connect:                  #如果该承诺含有对其他承诺的依赖，则 需要检查依赖承诺是否满足 满足则置为2  否则跳过
                con_id = int (connect[0])
                con_stat = int (connect[1])
                if s[con_id] == con_stat:
                    change = 2
                    (queue,transfers,Id,Repeat)=handel (st,i,change,'event',queue,transfers,Id,Repeat)
                else:
                    change = 4         #当前体条件过期时则转变为4
                    (queue,transfers,Id,Repeat)=handel (st,i,change,'event',queue,transfers,Id,Repeat) 
                    #状态转移处理函数，对状态队列，状态转移队列进行更新
                    
            else:               #如果该承诺不含有对其他承诺的依赖，则置为2 
                change = 2
                (queue,transfers,Id,Repeat)=handel (st,i,change,'event',queue,transfers,Id,Repeat)
                #状态转移处理函数，对状态队列，状态转移队列进行更新
                change = 4         #当前体条件过期时则转变为4
                (queue,transfers,Id,Repeat)=handel (st,i,change,'event',queue,transfers,Id,Repeat) 
                 #状态转移处理函数，对状态队列，状态转移队列进行更新
               
        elif c_stat == 2:
            change = 3      #该承诺的后果按时完成   则置为3
            (queue,transfers,Id,Repeat)=handel (st,i,change,'event',queue,transfers,Id,Repeat) 
             #状态转移处理函数，对状态队列，状态转移队列进行更新
            change = 5      #该承诺的后果过期   则置为5
            (queue,transfers,Id,Repeat)=handel (st,i,change,'event',queue,transfers,Id,Repeat)  
            #状态转移处理函数，对状态队列，状态转移队列进行更新  
              
    return (queue,transfers,Id,Repeat)
def handel (st,i,change,event,queue,transfers,Id,Repeat):
    s = st.S       #取出状态
    Id1 = st.Id
    new_s = list(s)    #复制状态
    new_s[i] = change   #状态跳转
    T = 1
    for j in range(len(Repeat)):     #检查是否重复
        status = Repeat[j].S
        if new_s == status:                #如果原来有重复则取出该状态对应的Id
            T = 0
            Id2 = Repeat[j].Id
    if T == 1:
        Id =Id +1
        Id2 = Id 
        st = St_node(Id2,new_s)   #生成新的的节点
        Repeat.append(st)
        queue.append(st)    #将新生成的状态加入子状态队列
    #M[Id1][Id2] = event     #将状态转移存入状态矩阵
    transfers.append([s,new_s,event])  #将跳转加入状态转移队列
 
    return (queue,transfers,Id,Repeat)   #将子状态队列与状态转移队列返回
                                       
def painting(transfers):
    G = pgv.AGraph(directed=True, strict=True, encoding='UTF-8')
    G.graph_attr['epsilon']='0.001'
    s = set({})
    for transfer in transfers:
        s.add(str(transfer[0]))
        s.add(str(transfer[1]))

    for node in list(s):
        G.add_node(node)

    for transfer in transfers:
        G.add_edge(str(transfer[0]), str(transfer[1]))

    G.layout('dot')
    G.draw('naive1.png')
# /anaconda/bin/python 
if __name__ == '__main__':
    c0 = Commitment([0, 'buy'], 'res0', '2017')
    c1 = Commitment(['04', 0], 'res1', '2018')
    c2 = Commitment(['13', 0], 'res2', '2019')
    c3 = Commitment(['24', 0], 'res3', '2020')
    c4 = Commitment(['33', 0], 'res3', '2020')
    c5 = Commitment(['33', 0], 'res3', '2020')
    c6 = Commitment(['44', 0], 'res3', '2020')
    c7 = Commitment(['54', 0], 'res3', '2020')
    c8 = Commitment(['63', 0], 'res3', '2020')

    cs = [c0,c1,c2]

    (transfers,Repeat) = create_state_transfers(cs)
 
   
    for line in transfers:
        print(line)
    print(len(transfers))
    #print(len(transfers))
    painting(transfers)
    #create_fsm('134', '123')


    
