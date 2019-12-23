# coding: utf8
import os
import re

from config.globals import debugLogger, G


def rewritingFile(**kwargs):
    '''
    path = G.OS_DIR + r'\config\globals.py'
    # D:\Project\pyut_outo_test\newRequestFarm\config\globals.py
    kwar = {'GlablasName':'Globals', 'Globalscenter':{'ISDICT_VARS':'999999', 'TBL_SLL_BEE': 'nihao'}, 'OSPATH': path}
    替换某个py文件中类的属性值，并返回结果替换后的结果
    :param kwargs: {varGlabals：要替换的类，ortherGlobals：{}， OSPATH：文件路径
    :return: 文件可迭代对象
    '''
    if not kwargs.get('GlablasName', None):
        raise ValueError('没有varGlabals这个键')
    elif not kwargs.get('Globalscenter', None):
        raise ValueError('没有ortherGlobals这个键')
    elif not kwargs.get('OSPATH',None):
        raise ValueError('没有ortherGlobals这个键')
    with open(kwargs.get('OSPATH'), 'r', encoding='UTF-8') as f:
        fileData = f.readlines()
    startSwith = 0
    endSwith = 0
    line = 1
    for i in fileData:

        if 'class ' + kwargs.get('GlablasName') in i:
             startSwith = line
        elif kwargs.get('GlablasName') + '()' in i:
             endSwith = line
        line += 1
    debugLogger.info('start:%s, end:%s' % (startSwith,endSwith))
    changeVarbial = kwargs['Globalscenter']
    for varbial in changeVarbial:
        for line in range(startSwith, endSwith):
            if varbial +' =' in fileData[line]:
                if '#' in fileData[line]:
                    fileData[line] = re.sub(r'=.*#', ' = '+changeVarbial[varbial] + " #", fileData[line] )
                else:
                    fileData[line] = re.sub(r'=.*$', ' = ' + changeVarbial['varbial'], fileData)


    return fileData


def removeFile(files, isDir=None):
    '''
    删除文件或删除文件夹下的所有文件
    :param file: 文件路径名或文件夹路劲名
    :param dir: 是否是文件夹，默认是文件
    :return:
    '''
    if isDir:
        if os.path.isdir(files):
            fileList = os.listdir(files)
            debugLogger.info('该文件夹下所有的文件为：%s' % str(fileList))
            for file in fileList:
                if os.path.isfile(file):
                    removeResult = os.remove(file)
        else:
            debugLogger.info('系统没有该文件夹路径，请确定参数是否正确')
            raise EnvironmentError
    else:
        if os.path.isfile(files):
            removeResult = os.remove(files)

        else:
            debugLogger.info('系统中没有该文件')
            raise EnvironmentError





if __name__ == '__main__':
    path = G.OS_DIR + r'\config\globals.py'
    # D:\Project\pyut_outo_test\newRequestFarm\config\globals.py
    kwar = {'GlablasName':'Globals', 'Globalscenter':{'ISDICT_VARS':'999999', 'TBL_SLL_BEE': 'nihao'}, 'OSPATH': path}
    debugLogger.info('nihaoa habazai=========================')
    rewritingFile(**kwar)
