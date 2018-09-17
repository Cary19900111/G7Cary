class Node(object):
    def __init__(self,score=None)
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
        len = len(x[0])
        split_rets = [z for z in map(lambda z:self._choose_split_point(x,y,idx,z),range(len)) if z is not None]
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


if __name__=='__main__':

            

