#enconding:utf-8
a=1
b=1
print('乘法口诀表:')
while a <= 9:
    while b <= a:
        print (b,'x',a,"=",a*b,' ',end='')
        b += 1
    print()
    b = 1
    a += 1

#enconding:utf-8
import random
random_num = random.randint(0,100)
i=1
num1 = input("请输入个随机整数: ")
num1 = int(num1)
while i < 5 :
    if num1 < random_num :
        print('猜小了')
        num1 = input("请输入个随机整数: ")
        num1 = int(num1)
        i +=1
    elif num1 == random_num :
        print('猜对了')
        break
    else :
        print('猜大了')
        num1 = input("请输入个随机整数: ")
        i +=1
        num1 = int(num1)
if i>5 :
    print('太笨了，下次再来')
