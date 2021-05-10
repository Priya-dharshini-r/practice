# Class is a blueprint or template for creating instances.
class Student:
	def __init__(self,s1, s2, s3, s4, s5):
		self.s1 = s1
		# print(self.s1)
		self.s2 = s2
		# print(self.s2)
		self.s3 = s3
		# print(self.s3)
		self.s4 = s4
		# print(self.s4)
		self.s5 = s5
		# print(self.s5)

	def marks(self,m1,m2,m3,m4,m5):
		self.m1 = m1
			# return self.m1
		self.m2 = m2
			# return self.m2
		self.m3 = m3
			# return self.m3
		self.m4 = m4
			# return self.m4
		self.m5 = m5
			# return self.m5

	def mark_in_five_subject(self):
		total = self.m1 + self.m2 + self.m3 + self.m4 + self. m5
		return total

	def percentage(self):
		total = self.mark_in_five_subject()
		percent = int((total/500) * 100)
		return percent

	def grades_for_each_subject(self):
		percent = self.percentage()
		if percent>=90 and percent<=100:
			return 'O'
		elif percent >=80 and percent <90:
			return 'A'
		elif percent>=70 and percent<80:
			return 'B'
		elif percent>=60 and percent<70:
			return 'C'
		elif percent>=50 and percent<60:
			return 'D'
		else:
			return "Fail!!"

	def isPass(self):
		total = self.mark_in_five_subject()
		# if total >= 50:
			# return True
		# else:
			# return False

		return total>=50


if __name__ == "__main__":
	# creating instances or objects for a class
	student1 = Student("DS","DBMS","Python","Java","OOPs")
	student2 = Student("DS","DBMS","Python","Java","OOPs")
	student1.marks(89,50,67,89,64)
	student2.marks(95,98,99,100,56)

	total = student1.mark_in_five_subject()
	grades = student1.grades_for_each_subject()
	percent1 = student1.percentage()
	graduated = student1.isPass()

	print(total, grades, graduated, percent1)

	total2 = student2.mark_in_five_subject()
	grades2 = student2.grades_for_each_subject()
	percent2 = student2.percentage()
	graduated2 = student2.isPass()

	print(total2, grades2, graduated2, percent2)













 
