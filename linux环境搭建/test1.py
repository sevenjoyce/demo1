# -*- coding:utf-8 -*-
import paramiko



HOST = '192.168.0.103'
PORT = '22'
USER = 'root'
PASSWD = '123456'
PACKAGE_DIR = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(HOST,PORT,USER,PASSWD)

'''
# 输入、输出、报错信息
stdin,stdout,stderr = ssh.exec_command('ifconfig')
# 返回对象
res = stdout.read().decode('utf8') #将结果读取byte格式，转换解码成utf8
print(res)
ssh.close()
'''

# 下载文件到本地
sftp = ssh.open_sftp()
# 下载
sftp.get('/home/tom/aaa', 'e:/')

# 上传
# sftp.put('', '')

ssh.close()