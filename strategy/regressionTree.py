import os
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
        for i in idx:
            xi,yi = x[i][feature],y[i]
            if xi<=split:
                split_sum[0]+=yi
                split_cnt[0]+=1
                split_sqrt_sum[0]+=yi**2
            else:
                split_sum[1]+=yi
                split_cnt[1]+=1
                split_sqrt_sum[1]+=yi**2
        split_avg = [split_sum[0]/split_cnt[0],split_sum[1]/split_cnt[1]]
        split_mse = [split_sqrt_sum[0]/split_cnt[0]-split_avg[0]**2,split_sqrt_sum[1]/split_cnt[1]-split_avg[1]**2]
        return sum(split_mse),split
    
    def _choose_split_point(self,x,y,idx,feature):
        unique = set([x[i][feature] for i in idx])
        if len(unique)==1:
            return None
        unique.remove(min(unique))
        mse,split = min((self._get_split_mse(x,y,idx,feature,split) for split in unique),key=lambda x:x[0])
        return mse,feature,split

    def _choose_feature(self,x,y,idx):
        m = len(x[0])
        split_rets = [z for z in map(lambda z:self._choose_split_point(x,y,idx,z),range(m)) if z is not None]
        if split_rets==[]:
            return None
        _,feature,split,split_avg = min(split_rets,key=lambda x :x[0])
        idx_split = [[],[]]
        while idx:
            i = idx.pop()
            xi = x[i][feature]
            if xi<split:
                idx_split[0].append(i)
            else:
                idx_split[1].append(i)
        return feature,split,split_avg,idx_split

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
                rule_right.append([nd.feature,-1,nd.split])
                que.append([nd.right,rule_right])
            
    def _expr_out(self,expr):
        feature,op,split = expr
        op = ">=" if op==1 else "<"
        return "Feature %d %s %.4f" % (feature,op,split)
    
    def fit(self,x,y,max_depth=5,min_samples_split=2):
        self.root=Node()
        que = [[0,self.root,list(range(len(y)))]]
        while que:
            depth,nd,idx = que.pop(0)
            if depth == max_depth:
                break
            if len(idx)<min_samples_split or set(map(lambda i :y[i],idx))==1:
                continue
            feature_rets = self._choose_feature(x,y,idx)
            if feature_rets is None:
                continue
            nd.feature,nd.split,split_avg,idx_split = feature_rets
            nd.left = split_avg[0]
            nd.right = split_avg[1]
            que.append([depth+1,nd.left,idx_split[0]])
            que.append([depth+1,nd.right,idx_split[1]])
            self.height=depth
            self._get_rule()

if __name__=='__main__':
    persons = pd.DataFrame(
        data=[['熊大',21,4,12000],
        ['车老二',25,5,15000],
        ['张三',23,6,20000],
        ['李四',28,8,35000]],
        columns=['name','age','grade','salary']
    )
    t = Tree()
    t._choose_feature(persons,persons['salary'],4)

