# -*- coding: utf-8 -*-
import os
import datetime
from .listdictAPI import  listdictAPI

imgExt = ['.bmp', '.gif', '.jpg', '.pic', '.png', '.tif', '.jpeg', '.php',\
          '.BMP', '.GIF', '.JPG', '.PIC', '.PNG', '.TIF', '.JPEG', '.PHP']


# html可以直接下载的文件类型
ExtDown = ['.zip', '.doc','.docx','.xls','.xlsx', '.rmvb', '.wmv']
   
# html可以直接打开浏览、播放的文件类型
ExtOpen = ['.txt', '.mp4','.pdf']
ExtOpen.append(imgExt)

class MyFile:
    """
        from myAPI.fileAPI import MyFile
        myfile = MyFile('blog/static/img/', ['.jpg'])
        imgs = myfile.toNameList()    
    """
    def __init__(self, dirpath, extlist):#extlist ＝［］获得指定目录下,全部目录名、文件名
        self.dirPath = dirpath # 目录路径 dirpath = '.../edustack/upvideo/testMyFile'
        self.extList = extlist # 指定类型的文件名列表extlist = ［'.txt'］获得全部扩展名为.txt文件名
        
    # 以列表形式，获得指定目录下，指定类型的全部文件名。extlist ＝［］获得指定目录下,全部目录名、文件名.    
    def toNameList(self):
        try:
            # 列表形式，返回指定目录下所有的文件和目录名（不含路径的短文件名）
            fileNames = os.listdir(self.dirPath)       
        except Exception as ex:
            """
            print(any([''])) # False
            print(any(['1'])) #True
            """
            print('Error execute: {}'.format(ex))
            # raise
            return ['']  # L1 = []与 L2 = [''] 区别：L1[0] 出错；L2[0] 不出错 2018.10.28    
        if (len(self.extList) > 0):
             fileNames = [fileName for fileName in fileNames 
                         if listdictAPI(self.extList, fileName).isListInStr()]
        filepathList = [os.path.join(self.dirPath, i) for i in fileNames 
                    if (not '._' in i)&(not '.DS' in i)] #（含路径的文件名）2016.10.24
        if filepathList == []:
            filepathList = ['']            
        return filepathList


def readtxt_to_list(filename):
    """
        功能：读文本文件（抛弃空行，删除左边空格），返回列表    
    """
    try:
        with open(filename,'r') as f:
            lines = f.readlines()
            return [l  for l in lines if l.strip()] # 抛弃空行 
    except Exception as ex:
        return ['']
        
def read_txt(filename):
    """
        功能：读文本文件（抛弃空行），返回字符串    
    """
    return ''.join(readtxt_to_list(filename))


def write_txt(filename, txt): 
    """
        功能：保存文本文件，适用于小文本文件
        w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    """   
    ret = False
    with open(filename,'w+') as f:
        f.write(txt)
        ret = True
    return ret




def upfile_save(mode, filepath):
    """
        保存上传文件：上传文件同名会覆盖
    """
    filename = os.path.join(filepath, mode.name)
    return savefile(mode, filename)

def upfile_save_2(upfile, filename1, filename2):
    """
        为了确保本地运行和部署后都能显示图像文件，上传文件到两个目录        
    """
    res1 = upfile_save(upfile, filename1) # 保存上传文件，供部署后，显示图像文件
    res2 = upfile_save(upfile, filename2) # 保存上传文件，供本地运行时，显示图像文件         
    return '%s. %s'%(res1,res2)

def upfile_save_time(mode, filepath):
    """
        保存上传文件：上传文件名添加当前时间，上传文件不会覆盖
    """
    name, etx = os.path.splitext(mode.name)
    filename = '%s-%s%s' %(name, datetime.datetime.now().strftime('%Y%m%d[%H:%M:%S]'), etx)  
    filename = os.path.join(filepath, filename)
    return savefile(mode, filename)
    
def savefile(mode, filename):    
    try:
        f = open(filename, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in mode.chunks():  # 分块写入文件  
            f.write(chunk)      
    except Exception as ex:
        return str(ex)    
    f.close() 
    return 'UpFile: %s. add nowTime. UpFile Success!' %(filename)  
    
def file_iterator(file_name, chunk_size=512):
    try:
        with open(file_name, 'rb') as f:   #python3   'rb'读二进制文件
            while True:
                c = f.read(chunk_size)
                if c: 
                    yield c                   
                else: 
                    break #return  okokok   
    except Exception as ex:
        yield ''      