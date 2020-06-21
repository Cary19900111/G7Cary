import configparser,sys,os
def readconfig(section=None,key=None):
    path_dir = os.path.split(os.path.realpath(__file__))[0]
    config = configparser.ConfigParser()
    config.read("{}/../config/config.ini".format(path_dir))
    return config.get(section,key)

# if __name__=='__main__':
#     print(read("qq",'qq_username'))