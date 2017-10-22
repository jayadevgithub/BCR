class SelfTest():
	def __init__(self,a):
		self.a = a 

	def print(self):
		print(self.a)

	def add(self,new_a):
		self.a = self.a +new_a


if __name__ == '__main__':
	self_test = SelfTest(2)
	self_test.print()
	self_test.add(3)
	self_test.print()
