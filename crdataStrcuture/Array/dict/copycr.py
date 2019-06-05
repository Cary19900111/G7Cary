from copy import copy,deepcopy
def copy_tutorial():
    '''
    第一层的id不一样，但是第二层的id是一样的，指向的是同一块地址
    修改copy1，就会修改copy2
    '''
    dict_in = {"name":"Cary","favor":["tabletennis","basketball"]}
    dict_copy1 = copy(dict_in)
    dict_copy2 = copy(dict_in)
    print("Before copy1:{}".format(dict_copy1))
    print("Before copy2:{}".format(dict_copy2))
    print(f"dict_in id is {id(dict_in)}")
    print("dict_copy1 id is %d" %id(dict_copy1))
    print("dict_copy2 id is %d" %id(dict_copy2))
    dict_copy1["favor"].append("footb")
    print("After copy1:{}".format(dict_copy1))
    print("After copy2:{}".format(dict_copy2))
    print("dict_copy1.favor id is %d" %id(dict_copy1["favor"]))
    print("dict_copy2.favor id is %d" %id(dict_copy2["favor"]))

def deepcopy_tutorial():
    '''
    第一层的id不一样，并且第二层的id也是不一样的,所以一般我们的复制都用deepcopy
    返回一个完全独立变量
    '''
    dict_in = {"name":"Cary","favor":["tabletennis","basketball"]}
    dict_copy1 = deepcopy(dict_in)
    dict_copy2 = deepcopy(dict_in)
    print("Before copy1:{}".format(dict_copy1))
    print("Before copy2:{}".format(dict_copy2))
    print(f"dict_in id is {id(dict_in)}")
    print("dict_copy1 id is %d" %id(dict_copy1))
    print("dict_copy2 id is %d" %id(dict_copy2))
    dict_copy1["favor"].append("footb")
    print("After copy1:{}".format(dict_copy1))
    print("After copy2:{}".format(dict_copy2))
    print("dict_copy1.favor id is %d" %id(dict_copy1["favor"]))
    print("dict_copy2.favor id is %d" %id(dict_copy2["favor"]))
if __name__=="__main__":
    deepcopy_tutorial()
