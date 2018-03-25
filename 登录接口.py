# Author：李捷豪
# Time：2018.3.25
# Version:Python3.6
# Tools :Pycharm 2017.3.2


# 注册函数
def sign_up():
    userdata = open("userdata.txt",'a+')
    username = input("请设定您的用户名:")
    password = input("请设定您的密码:")
    userdata.writelines(username+','+password+',0\n')       # 这里的0就是lock_flag
    userdata.close()
    print(username,password)
    print("恭喜你完成了注册!\n")

# 锁定函数(更新lock_flag函数)
def lock(username,lock_flag):
    f = open("userdata.txt","r")
    lines = f.readlines()                 # 先把数据文件用自读形式读入内存，存于 lines 列表中
    f.close()
    f_w = open("userdata.txt","w")        # 把数据文件用只写形式打开，这样子等一下写入时会先清空原文件再重新写入
    n = 0                                 # 索引变量
    for line in lines:                    # 查找出对应的用户名在lines列表中的索引
        dataline = line.split(",")
        if username == dataline[0]:
            n = lines.index(line)
            break
    name = dataline[0]
    password = dataline[1]
    flag = lock_flag
    new = name+","+password+","+str(flag)+"\n"
    lines[n] = new                         #把该元素更新
    for i in lines:
        f_w.writelines(i)                 #把lines列表重新写入userdata.txt文件中
    f_w.close()

# 登录验证 函数
def sign_in(name, password):
    userdata = []
    f = open("userdata.txt",'r')
    readlines = f.readlines()
    for userline in readlines:
        userdata = userline.split(",")
        username = userdata[0]
        userpassword = userdata[1]
        lock_flag = int(userdata[2].strip("\n"))
        if name == username:                          # 情况4：用户已被锁定
            if lock_flag >= 3:
                return [-1,lock_flag]
            if password == userpassword:              # 情况2：登录成功
                lock_flag = 0
                lock(name, lock_flag)
                return [1,lock_flag]
            elif password != userpassword:            # 情况3：密码输入错误
                lock_flag += 1
                lock(name,lock_flag)
                return [2,lock_flag]
    else:                                             # 情况1：找不到该用户
        return [0]
    f.close()

# 主程序
while True:
    print("程序选项如下")
    print("1.注册   2.登录   3.退出程序")
    i = input("请输入想做的事情对应的序号：")
    if i == '1':                                  # 程序选项1：注册
        sign_up()
    elif i == '2':                                # 程序选项2：登录
        username = input("请输入您的用户名:")
        password = input("请输入您的密码:")
        flag = sign_in(username, password)
        if flag[0] == 0:
            print("找不到该用户，请重新输入\n")
        elif flag[0] == 1:
            print("恭喜你，登录成功！\n")
        elif flag[0] == 2:
            print("第"+ str(flag[1])+"次密码输入错误，连续输入密码错误超过3次该用户将被锁定\n")
        elif flag[0] == -1:
            print("抱歉，该用户已被锁定\n")
    elif i == '3':                               # 程序选项3：退出程序
        print("已退出程序，谢谢\n")
        exit()
    else:
        print("输入错误，请重新输入\n")


