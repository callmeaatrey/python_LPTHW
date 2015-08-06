from sys import exit 
import os
import time

# class to return what to do
class Menu(object):
	def choice(self):
		print "Hello. I am here to do your calculations. So, what do you want to do first:"
		print "1. Add n numbers"
		print "2. Find the difference of 2 numbers"
		print "3. Product of n numbers"

		menu_choice = int(raw_input('[choice] '))

		return menu_choice

class Functions(object):
	def add(self, n):
		sum_value = 0
		if n == 0:
			print "Nothing to do the addition on!"
		elif n < 0:
			print "Error in number entered"
		else:
			for i in range(1, n):
				sum_value += i
			print "The sum of the numbers is : ", sum_value
	def diff(self, n):
		sub_list = []
		sub_value = 0
		if n == 0:
			print "There is nothing to subtract from nothing!"
		elif n < 0:
			print "Error in number entered"
			exit(0)
		else:
			print "Enter the numbers:"
			a = int(raw_input('[value 1] '))
			b = int(raw_input('[value 2] '))
			sub_value = a - b
			print "The difference is: ", sub_value

	def product(self, n):
		prod_value = 1
		prod_list = []
		if n == 0:
			print "Nothing to multiply"
		elif n < 0:
			print "Error in number entered"
			exit(0)
		else:
			print "Enter the numbers: "
			for i in range(1, n):
				b = long(raw_input('[value] '))
				prod_list.append(b)
				prod_value *= b
			print "The product is: ", prod_value

class Path(object):
	def __init__(self):
		self.menu = Menu()
		self.functions = Functions()

	add_list = []

	def menu_call(self):
		user_choice = self.menu.choice()
		if user_choice == 1:
			self.functions.add(100)
		if user_choice == 2:
			self.functions.diff(3)
		if user_choice == 3:
			self.functions.product(4)
		else:
			print "Wrong Choice!"

call = Path()
call.menu_call()