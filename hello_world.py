print("hello world");
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用
print(list[2]);
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])# 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print(tinydict['name'])

num = 2
if num == 3:            # 判断num的值
    print ('boss')
elif num == 2:
    print ('user')
elif num == 1:
    print ('worker')
elif num < 0:           # 值小于零时输出
    print ('error')
else:
    print ('roadman')    # 条件均不成立时输出

count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1

print("Good bye!")
for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter);
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前字母 :', fruit)
print("Good bye!")

import os

# 给出当前的目录
print(os.getcwd());
