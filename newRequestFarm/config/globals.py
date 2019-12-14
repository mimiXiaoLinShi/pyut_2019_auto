#!python

import datetime
import os
import logging
import sys
# from imp import reload
#
# reload(sys)
# sys.setdefaultencoding('utf8')
from lib.utils import tcpSocket

OS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(OS_DIR)


class Globals:
    OS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ISDICT_VARS = 2 # 必填
    # ISDICT_VARS = 2
    ENV_CLASS = 3
    LogErver = logging.INFO

G = Globals()

class VcnGlobals:
    TEST_BED = 'TBL_MUTEST_BED'
    TBL_SLL_BEE = 2

class VcmGlobals:
    TEST_BED = 'TBL_MUTEST_BED'
    TBL_SLL_BEE = 2

def getLogger(pathName):
    get_logget = logging.getLogger(pathName)      #创建一个logger对象，它提供了应用程序可以直接使用的接口，其类型为“<class 'logging.RootLogger'>”；
    formater = logging.Formatter(
        '%(asctime)s|%(levelname)s|%(message)s')  # 自定义日志的输出格式，这个格式可以被文件输出流和屏幕输出流调用；
    sh = logging.StreamHandler(sys.stdout)  # 创建一个屏幕输出流；
    sh.setFormatter(formater)     # 运用输出流的输出格式
    get_logget.addHandler(sh)
    logpath = os.path.abspath(G.OS_DIR + '/log')
    if os.path.exists(logpath) == False:
        os.makedirs(logpath)
    logpath = os.path.join(logpath, '%s.log' % pathName)
    fh = logging.FileHandler(logpath)  # 创建一个文件输出流；
    fh.setFormatter(formater)       # 创建文件输出流的输出格式
    get_logget.addHandler(fh)
    get_logget.setLevel(G.LogErver)
    # logging.basicConfig(level=G.LogErver,
    #                     filename=path,
    #                     datefmt='%Y/%m/%d %H:%M:%S',
    #                     format='%(asctime)s-%(filename)s-%(levelname)s-%(message)s')
    # logger = logging.getLogger(__name__)
    return get_logget


path = 'run_'+ datetime.datetime.now().strftime('%Y%m%d')
debugLogger = getLogger(path)

# si = tcpSocket('192.168.1.252', 1000, 'nihaoaaaaaa')
