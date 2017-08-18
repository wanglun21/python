#coding:utf-8
print ("9月23日是我大女儿王涵蕊的生日，我想办个聚会")
keren = ["姥爷",'姥娘',"奶奶"]
print ("敬请\n  "+keren [0],"参加聚会")
print ("敬请\n  "+keren [1],"参加聚会")
print ("敬请\n  "+keren [2],"参加聚会")
laoniang = keren.pop(1)
print (laoniang + "有事来不了了，我们非常遗憾")
keren.append ("叔叔")
print ("现在我们邀请"+ keren [2],"参加我们的聚会")
print ("敬请\n  "+ keren [2],"参加聚会")
print ("我又订了一个大桌子，可以邀请更多的朋友来参加聚会了")
keren.insert(0,"张老师")
keren.insert(2,"婶子")
keren.append("弟弟")
print ("敬请\n  "+keren [0],"参加聚会")
print ("敬请\n  "+keren [1],"参加聚会")
print ("敬请\n  "+keren [2],"参加聚会")
print ("敬请\n  "+keren [3],"参加聚会")
print ("敬请\n  "+keren [4],"参加聚会")
print ("敬请\n  "+keren [5],"参加聚会")
print ("非常非常抱歉！！我订的桌子到不了了\n我只能邀请两位参加聚会了")
print (keren.pop(0)+"：非常抱歉，我们无法邀请您了！")
print (keren.pop(1)+"：非常抱歉，我们无法邀请您了！")
print (keren.pop(2)+"：非常抱歉，我们无法邀请您了！")
print (keren.pop(2)+"：非常抱歉，我们无法邀请您了！")
print (keren[0],keren[1]+"你们仍在受邀行列，请准时参加")
del keren[0]
del keren[0]
print(keren)



