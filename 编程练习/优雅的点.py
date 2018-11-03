#题目描述
# 小易有一个圆心在坐标原点的圆，小易知道圆的半径的平方。小易认为在圆上的点而且横纵坐标都是整数的点是优雅的，小易现在想寻找一个算法计算出优雅的点的个数，请你来帮帮他。
# 例如：半径的平方如果为25
# 优雅的点就有：(+/-3, +/-4), (+/-4, +/-3), (0, +/-5) (+/-5, 0)，一共12个点。

# 输入描述:
# 输入为一个整数，即为圆半径的平方,范围在32位int范围内。
# 输出描述:
# 输出为一个整数，即为优雅的点的个数
#-*- coding:utf-8 -*-
import math
r_square=int(raw_input())
r1=int(math.sqrt(r_square))
count=0

if r1*r1==r_square:
	count+=4
	r1-=1
for i in range(1,r1+1):
	x=int(math.sqrt(r_square-i*i))
	if i*i+x*x==r_square:
		count+=4
print(count)
