class KDvector2:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def add(self, v2):
		final_x = self.x + v2.x
		final_y = self.y + v2.y
		return KDvector2(final_x, final_y)

	def printvector(self):
		print(self.x, self.y)



if __name__ == "__main__":
	v1 = KDvector2(2, 3)
	v2 = KDvector2(5, 10)
	v3 = v1.add(v2)
	v3.printvector()
