#coding:utf-8
import os


def find_files(path):
    files=os.listdir(path)
    for file in files:
        yield file
def genLabel():
    with open('cl.txt','w') as f:
        for file in find_files('./rect/'):
            f.write(file+' 0\n')
        for file in find_files('./circle/'):
            f.write(file+' 1\n')
if __name__=='__main__':
    genLabel()