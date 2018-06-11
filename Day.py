# Day.py
n=input("请输入今天星期几（1-7）：")
day="montuewedthufrisatsun"
pos=(int(n)-1)*3
print("星期简写为："+day[pos:pos+3]+".")
