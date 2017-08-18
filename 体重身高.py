# -*- coding: utf-8 -*-
height = float (input ("请输入您的身高(单位:米)"))
weight = float (input ("请输入您的体重(单位:千克)"))
bmi = weight/(height**2)
print ("您的身高是：",height,"米")
print ("您的体重是：",weight,"千克")
print ("根据BMI公式计算，您的体型：")
if bmi >= 32:
	print ("严重肥胖\n请抓紧减肥")
elif bmi >= 28:
	print ("肥胖\n请注意减肥")
elif bmi >= 25:
	print ("过重\n请注意锻炼")
elif bmi >= 18.5:
	print ("正常\n请注意保持")
else:
	 print("过轻\n请注意营养")
	  
 
