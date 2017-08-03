import time;  # 引入time模块

ticks = time.time()
print("当前时间戳为:", ticks)
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
import calendar

cal = calendar.month(2017, 2)
print("以下输出2017年2月份的日历:")
print(cal)


# 定义函数
def printme(str):
    #"打印任何传入的字符串"
    print(str);
    return;


# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");

import support;
support.print_func("Luke")

str = input("请输入：");
print("你输入的内容是: ", str);

# 打开一个文件
fo = open("foo.txt", "wb")
print("文件名: ", fo.name);
print("是否已关闭 : ", fo.closed);
print("访问模式 : ", fo.mode);
fo.close();
print("是否已关闭 : ", fo.closed);
