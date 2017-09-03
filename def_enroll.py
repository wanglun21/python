def enroll (name , gender , age = 6 , city = "qingdao"):
	print ("name:" , name)
	print ("gender:" , gender)
	print ("age:", age)
	print ("city:" , city)
enroll ("xiaoming","F")
enroll ("xiaoming","F",6,"jinan")
enroll ("xiaoming","F",city = "jinan")

def person (name , age , **other):
	print ("name:", name ,"\nage:", age , "\nother:", other)
person("joy",3,city="jinan")




	
	
