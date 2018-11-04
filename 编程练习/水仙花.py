# 输出描述:
# 对于每个测试实例，要求输出所有在给定范围内的水仙花数，就是说，输出的水仙花数必须大于等于m,并且小于等于n，如果有多个，则要求从小到大排列在一行内输出，之间用一个空格隔开;
# 如果给定的范围内不存在水仙花数，则输出no;
# 每个测试实例的输出占一行。
# 示例1
# 输入
# 复制
# 100 120
# 300 380
# 输出
# 复制
# no
# 370 371

[m,n] = [int(i) for i in raw_input().split(' ')]
result =[]
for i in range(m,n+1):
    x = i/100
    y = (i-100*x)/10
    z = i -100*x -y*10
    if x**3 +y**3 +z**3 ==i:
        result.append(i)
if result != []:
    print(' '.join([str(i) for i in result]))
else:
    print('no')