import os
from copy import copy
import numpy as np 
import pandas as pd
import tushare as ts
class Node(object):
    def __init__(self,score=None):
        self.score = score
        self.left = None
        self.right = None
        self.split = None
        self.feature = None

class Tree(object):

    def __init__(self):
        self.root = Node()
        self.height = 0
    
    def _get_split_mse(self,x,y,idx,feature,split):
        split_sum = [0,0]
        split_cnt = [0,0]
        split_sqrt_sum = [0,0]
        try:
            for i in idx:
                xi,yi = x.loc[i,feature],y[i]
                if xi<split:
                    split_sum[0]+=yi
                    split_cnt[0]+=1
                    split_sqrt_sum[0]+=yi**2
                else:
                    split_sum[1]+=yi
                    split_cnt[1]+=1
                    split_sqrt_sum[1]+=yi**2
            split_avg = [split_sum[0]/split_cnt[0],split_sum[1]/split_cnt[1]]
            split_mse = [split_sqrt_sum[0]/split_cnt[0]-split_avg[0]**2,split_sqrt_sum[1]/split_cnt[1]-split_avg[1]**2]
        except Exception as err:
            print(x)
            print(idx)
            print(split)
        return sum(split_mse),split,split_avg
    
    def _choose_split_point(self, x, y, idx, feature):
        unique = set([x.loc[i,feature] for i in idx])
        if len(unique) <= 1:
            return None
        if len(unique) == 2:
            unique_list =  list(unique)
            split = (unique_list[0]+unique_list[1])/2
            mse,split,split_avg = self._get_split_mse(x,y,idx,feature,split)
        else:
            unique.remove(min(unique))
            unique.remove(max(unique))   
            mse,split,split_avg = min((self._get_split_mse(x,y,idx,feature,split) for split in unique),key=lambda x:x[0])
        return mse, feature, split,split_avg

    def _choose_feature(self, x, y, idx):
        m = x.columns
        m_len = len(m)
        split_rets = [z for z in map(lambda z:self._choose_split_point(x, y, idx, m[z]), range(m_len)) if z is not None]
        if split_rets == []:
            return None
        _, feature, split,split_avg = min(split_rets, key=lambda x: x[0])
        idx_split = [[], []]
        while idx:
            i = idx.pop()
            xi = x.loc[i,feature]
            if xi < split:
                idx_split[0].append(i)
            else:
                idx_split[1].append(i)
        return feature, split, idx_split,split_avg

    def _get_rule(self):
        que = [[self.root,[]]]
        self.rules = []
        while que:
            nd,exprs = que.pop(0)
            if not (nd.left or nd.right):
                literals = list(map(self._expr_out,exprs))
                self.rules.append([literals,nd.score])
            if nd.left:
                rule_left = copy(exprs)
                rule_left.append([nd.feature,-1,nd.split])
                que.append([nd.left,rule_left])
            if nd.right:
                rule_right = copy(exprs)
                rule_right.append([nd.feature,1,nd.split])
                que.append([nd.right,rule_right])
            
    def _expr_out(self,expr):
        feature,op,split = expr
        op = ">=" if op==1 else "<"
        return "Feature %s %s %.4f" % (feature,op,split)
    
    def print_rules(self):
        for i, rule in enumerate (self.rules):
            literals, score = rule
            print("Rule %d: " % i, ' | '.join(literals) + ' => split_hat %.4f' % score)
    
    def fit(self,x,y,max_depth=5,min_samples_split=2):
        self.root = Node()
        que = [[0, self.root, x.index.tolist()]] 
        while que:
            depth, nd, idx = que.pop(0) 
            if depth == max_depth:
                break 
            if len(idx) < min_samples_split or set (map (lambda i: y[i], idx)) == 1:
                continue 
            feature_rets = self._choose_feature(x, y, idx)
            if feature_rets is None:
                continue 
            nd.feature, nd.split, idx_split, split_avg = feature_rets
            nd.left = Node(split_avg[0])
            nd.right = Node(split_avg[1])
            que.append([depth+1, nd.left, idx_split[0]])
            que.append([depth+1, nd.right, idx_split[1]]) 
            self.height = depth
        self._get_rule()

if __name__=='__main__':
    persons = pd.DataFrame(
        data=[['熊大',21,4,12000],
        ['车老二',22,5,15000],
        ['张三',23,6,20000],
        ['李四',24,7,35000],
        ['dfsf',34,5,17000],
        ['fdaf',21,3,9000],
        ['fdsfa',19,5,13000],
        ['gfdg',30,4,12000],
        ['hjgj',23,7,14000],
        ['qweq',26,34,15400],
        ['ytu',23,6,20000],
        ['zcxxzc',28,8,40000]],
        columns=['name','age','grade','salary']
    )
    #person_list = persons.values
    #print(a)
    #print(persons)
    t = Tree()
    data = persons.loc[:,["salary","age","grade"]]
    # x列表，y要预测的列，idx行索引
    t.fit(data.loc[:,["age","grade"]],data["salary"])#,persons.index.tolist())
    t.print_rules()
