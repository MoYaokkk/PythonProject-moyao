"""
补充知识点:
    break: 直接结束循环
    continue: 跳过本次循环,继续下次循环
猜数字游戏分析
    1.系统随机1-100的数字作为底数
    2.让用户无限猜,直到猜对为止
    3.每次判断用户猜的数和底数的大小,并给出提示
"""
# 1.系统随机1 - 100的数字作为底数
import random
rand_num = random.randint(1,100)
print(f"只有内部人员知道的底数{rand_num}")
# 2.让用户无限猜, 直到猜对为止
while True:
    guess_num = int(input('请输入您本次猜的数(1-100):'))
    # 3.每次判断用户猜的数和底数的大小, 并给出提示
    if 1 <= guess_num <= 100:
        if guess_num > rand_num:
            print('猜大了')
        elif guess_num < rand_num:
            print('猜小了')
        else:
            print('恭喜,猜对了!')
            break
    else:
        print('你输入的数字不符合要求,请猜1-100之间:')
