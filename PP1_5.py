'''
    Lesson: Typecasting
    Author: Karcihan Satheskishan
    Date Created: Sept 23, 2024
    Date Last Modified: Sept 24, 2024
'''
def q1():
  num = input("Input an integer: ")
  num = int(num)
  num += 3
  print(num)

def q2():
  num = input("Input a number: ")
  num = str(num) + "4"
  num = float(num)
  num = (num + 2)
  print(num)

def q3():
  rad = input("Input a radius: ")
  rad = float(rad)
  area = (3.14 * rad * rad)
  print(area)

def q4():
  num = input("Input a number: ")
  num = float(num)
  num = (num * 12)
  num = int(num)
  print(num)

def q5():
  var = input("Input an integer: ")
  var = int(var)
  var = (var + 5)
  print(f"Your number + 5 is {var}")
#Comment this code out when running tests
#Do not comment this out when running your program normally

# q1()
# q2()
# q3()
# q4()
# q5()
