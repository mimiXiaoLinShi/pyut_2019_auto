# coding: utf8
import time
from binascii import b2a_hex

import paramiko

from newRequestFarm.config.globals import debugLogger


class SSHConnection:

    def create_obj(self):
        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 目的是接受不在本地Known_host文件下的主机。

    def create_invoke(self):
        self._chan = self._ssh.invoke_shell()  # 新创建通道

    def exec_command(self, cmd, pramcails='', timeOut=60):
        if not cmd.endswith('\n'):
            command = cmd + '\n'
        else:
            command = cmd

        # try:
        self._chan.send(command)
        self._chan.settimeout(timeOut)
        time.sleep(1)
        shut = self._chan.recv(5000).decode('utf-8')
        counte = 0
        if cmd in shut:
            while self.deal_result(shut, pramcails):
                counte += 1
                getshut = self._chan.recv(5535).decode('utf-8')
                shut += getshut
                if counte > 10:
                    debugLogger.info('最多只接受10次，如有未接收完的数据请更改参数')
                    break

        su = self.parsingGet(shut)
        return su

        # except Exception as e:
        #     print(e)
        #     debugLogger.info('连接超时')
        #     raise

    def parsingGet(self, shut):
        debugLogger.info('解析前：%s' % shut)
        try:
            resultLens = shut.replace("\r\r\n", "\r\n").replace('[m[K', '').replace('[01;31m[k',
                                                                                                            '').replace(
                '[k', '').split('\r\n')

        except UnicodeDecodeError as e:
            resultLens = shut.decode('utf-8', errors='ignore').replace("\r\r\n", "\r\n").replace('[m[K', '').replace(
                '[01;31m[k', '').split('\r\n')

        result = [line.replace('\r', '') for line in resultLens[1:]]
        debugLogger.info('解析后 %s' % result)
        return result

    def deal_result(self, endStr, pramcails):
        if pramcails:
            if endStr.endswith(pramcails.encode('utf-8')):
                return False
            else:
                return True
        if endStr.endswith('[k') or endStr.endswith('~# ') or endStr.endswith(
                '# ') or endStr.endswith(':~$ ') or endStr.endswith(
            '~#[m') or endStr.endswith('~#[m[k[') or endStr.endswith(
            '$[0;39m') or endStr.endswith(':null') or endStr.endswith(
            'password') or endStr.endswith('password ') or endStr.endswith(
            ']') or b2a_hex(buff)[-6:] == 'lb5b4b':
            return False

        return True

    def shcanRoot(self, supername, superpassword):
        self._chan.send(supername)
        buff = self._chan.recv(5535)
        i = 1
        while True:
            if buff.endswith('password: ').encode('utf-8'):
                self._chan.send(superpassword)
                if self._chan.recv('$ ').decode('utf-8'):
                    debugLogger.debug('切换root成功')
                    break

            buff += self._chan.recv(3553)
            i += 1
            if i == 5:
                debugLogger.info('切换root失败')
                raise ValueError('切换root失败')



    # def deal_result(self, data, pramcails=''):
    #     if pramcails:
    #         if data.endswith(pramcails):
    #             return False
    #     if data.endswith('~# ') or data.endswith('[ '):
    #         return False

    def connection(self, ip, port, username, password, isRoot='', superusername='', superpassword=''):
        '''

        :param self:
        :param ip: 连接后台ip
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        :param isRoot: 是否切换root用户
        :param superusername: root用户名
        :param superpassword: root密码
        :return:
        '''
        self.create_obj()
        self._ssh.connect(ip, int(port), username, password)
        self.create_invoke()
        if isRoot:
            self.shcanRoot(superusername, superpassword)

        self._chan.send('timeout=0\n')
        self._chan.recv(5535)

    def command(self, command, dockername=None, pramcails='', timeOut=60):

        result = self.exec_command(command, timeOut=timeOut)
        # debugLogger.info(result)
        return result


if __name__ == '__main__':
    ssh = SSHConnection()
    ssh.connection('114.55.126.96', 22, 'root', 'Aliyun2019')
    pwd = ssh.command('pwd')
    ll = ssh.command('ll')
    # print(type(pwd))
    # print('--------------------------')
    # print(type(ll))
    # print('99999999999999999999999999')
    # print(pwd)
    # print('===============')
    # print(ll)
    # ssh.command('docker ps')
