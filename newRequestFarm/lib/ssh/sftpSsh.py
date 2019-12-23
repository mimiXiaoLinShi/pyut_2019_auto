# coding:utf8
import paramiko

from globals import debugLogger


def linux_to_windows(localPath, remotePath, server_ip, server_port, server_user, server_password, isFile = ''):
    '''
    重远程服务器下载文件到本地
    :param localPath:
    :param remotePath:
    :param server_ip:
    :param server_port:
    :param server_user:
    :param server_password:
    :param isFile:
    :return:
    '''
    import os
    try:
        print(localPath)
        print(remotePath)
        client = paramiko.Transport(server_ip, int(server_port))
        client.connect(username=server_user, password=server_password)
        sftp = paramiko.SFTPClient.from_transport(client)
    except Exception as e:
        debugLogger.info('sfpt连接出错 %s' % e)
        raise

    if isFile:
        files = sftp.listdir(remotePath)
        for f in files:
            for i in sftp.listdir_attr(remotePath):
                print(i.__dict__)
                f = i.__dict__["filename"]
                fT = i.__dict__['longname'].split(' ')[0]
                if 'd' in fT:
                    continue
                print('-----')
                print(f)
                sftp.get(os.path.join(remotePath, f).replace('\\', '/'), os.path.join(localPath, f).replace('\\', '/'))
    else:
        sftp.get(remotePath, localPath)
        return 0


def win_to_liunx(localPath, remotePath, server_ip, server_port, server_user, server_password):
    try:
        print(localPath)
        print(remotePath)
        client = paramiko.Transport(server_ip, int(server_port))
        client.connect(username=server_user, password=server_password)
        sftp = paramiko.SFTPClient.from_transport(client)
    except Exception as e:
        debugLogger.info('sfpt连接出错 %s' % e)
        raise
    sftp.put(localPath, remotePath)
    return 0


if __name__ == '__main__':
    # linux_to_windows(r'D:\log'.encode('utf-8').decode('utf-8'), '/home/Desktop'.encode('utf-8').decode('utf-8'), '114.55.126.96', '22', 'root', 'Aliyun2019',isFile=90)
    win_to_liunx(r'D:\log\nihao.txt'.encode('utf-8').decode('utf-8'), '/home/Desktop/nihao.txt'.encode('utf-8').decode('utf-8'), '114.55.126.96', '22', 'root', 'Aliyun2019')


