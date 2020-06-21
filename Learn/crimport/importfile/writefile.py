from .createfile import fs
#单例模式，已经在importfile导入过一次
def wfile():
    fs.write("testimport")
