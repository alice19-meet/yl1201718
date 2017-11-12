

class Animal(object):
	def __init__(self, sound,name,age,gender,favorite_color,favorite_food):
		self.sound=sound
		self.name=name
		self.age=age
		self.gender=gender
		self.favorite_color=favorite_color
		self.favorite_food=favorite_food

	def eat(self,food):
		print('Yummy!!'+self.name+' is eating '+ food)

	def description(self):
		print(self.name+'_is_'+self.age+'years old and loves the color'+self.favorite_color)


a=Animal('woof',' Bella','1 ','female','white','hamburgers')
a.eat('hamburgers')
a.description()
