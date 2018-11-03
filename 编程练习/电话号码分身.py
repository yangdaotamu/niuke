# 题目描述
# 继MIUI8推出手机分身功能之后，MIUI9计划推出一个电话号码分身的功能：首先将电话号码中的每个数字加上8取个位，然后使用对应的大写字母代替 （"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"）， 然后随机打乱这些字母，所生成的字符串即为电话号码对应的分身。
# 输入描述:
# 第一行是一个整数T（1 ≤ T ≤ 100)表示测试样例数；接下来T行，每行给定一个分身后的电话号码的分身（长度在3到10000之间）。
# 输出描述:
# 输出T行，分别对应输入中每行字符串对应的分身前的最小电话号码（允许前导0）。
# 示例1
# 输入
# 复制
# 4
# EIGHT
# ZEROTWOONE
# OHWETENRTEO
# OHEWTIEGTHENRTEO
# 输出
# 复制
# 0
# 234
# 345
# 0345

nTotal = int(raw_input())
  
for x in xrange(0,nTotal):
  
    data = raw_input()
  
    Zero_Count = data.count('Z')
  
    Two_Count = data.count('W')
  
    Four_Count = data.count('U')
  
    Six_Count = data.count('X')
  
    Eight_Conut = data.count('G')
  
    Three_Count = data.count('H') - Eight_Conut
  
    Five_Conut = data.count('F') - Four_Count
  
    Seven_Count = data.count('S') - Six_Count
  
    One_Count = data.count('O') - Zero_Count - Two_Count - Four_Count
           
    Nine_Count =  data.count('I') - Five_Conut - Six_Count - Eight_Conut
  
    print "0"*Eight_Conut + "1"*Nine_Count + "2"*Zero_Count + "3"*One_Count + "4"*Two_Count + "5"*Three_Count + "6"*Four_Count + "7"*Five_Conut + "8"*Six_Count + "9"*Seven_Count
