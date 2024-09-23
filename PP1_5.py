'''
    Lesson: Typecasting
    Author: Karcihan Satheskishan
    Date Created: Sept 23, 2024
    Date Last Modified: Sept 23, 2024
'''
def q1():
  num = input("Enter an integer: ")
  num = int(num)
  num += 3
  print(num)

def q2():
  num = input("Enter a number: ")
  num = (num + "4")
  num = float(num)
  num += 2
  print(num)

def q3():
  rad = input("Enter a radius: ")
  rad = float(rad)
  area = (3.14 * rad * rad)
  print(area)

def q4():
  num = input("Enter a number: ")
  num = float(num)
  num = (num * 12)
  num = int(num)
  print(num)

def q5():
  num = input("Enter a number: ")
  num = int(num)
  num += 5
  print(f"Your number + 5 is {num}.")
#Comment this code out when running tests
#Do not comment this out when running your program normally

#q1()
#q2()
#q3()
#q4()
#q5()
