# -*- coding: utf-8 -*-
count = 0
def hanoi (n,A,B,C):
	global count  
	if n == 0:
		return
	else:
		hanoi(n-1,A,C,B)
		print ("移动第"+ str(n) + "个盘子" + A + "===>" + C)
		count += 1
		hanoi(n-1,B,A,C)
hanoi (1,"A","B","C")
print ("总共移动" + str(count) + "步")
