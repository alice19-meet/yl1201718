class Person(object):
	def __init__(self, city,name,age,gender,favorite_color,favorite_food):
		self.city=city
		self.name=name
		self.age=age
		self.gender=gender
		self.favorite_color=favorite_color
		self.favorite_food=favorite_food

	def eat(self):
		print(self.name+' is eating '+self.favorite_food)

	def read(self):
		print(self.name+' is reading a book.')

r=Person('New York','Rahaf','15','girl','blue','eggs')
r.eat()
r.read()

class Song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics
	def sing_me_a_song(self):
		for value in self.lyrics:
			print (value)

flower_song=Song(['Roses are red,',
	'Violets are blue,',
	'I wrote this poem for you.'])
flower_song.sing_me_a_song()