
import random
from urllib import response, request
import json
import time

def sleep(n_secs):
    time.sleep(n_secs)

# 生成随机email，RuoYi创建用户时调用
def AutoEmail():
    email = ""
    for i in range(10):
        n = random.randint(0, 9)
        email = email + str(n)
    return email + "@qq.com"


# 生成随机用户昵称/名称，RuoYi创建用户时调用
def AutoNickName():
    nickname = ""
    for i in range(5):
        name = random.randint(0, 9)
        nickname = nickname + str(name)
    return "Auto用户名/昵称" + nickname


# 生成随机手机号，RuoYi创建用户时调用
def AutoPhonenumber():
    phonenumber = ""
    for i in range(10):
        n = random.randint(0, 9)
        phonenumber = phonenumber + str(n)
    return "1" + phonenumber


# 从response中提取cookie
def get_cookie(request):
    response.login_cookie = request.headers["Cookie"]

# 获取一个13位数的时间戳
def getTimeStamp():
    return int(time.time() * 1000)

#文件读取
def get_export_files_jd():
    with open('demo/1634397091476.xlsx', 'rb')as f:
        files = f.read()
    return files

def get_file(filePath="demo/1634397091476.xlsx"):
    return open(filePath, "rb")