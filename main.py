# # --------- ex1 and ex2 ------------
# # print(x+y)
# # print(x/y)
# # print("Difference of x and y is:", x-y)
# # print("x*y=:"+ x*y)
# #  print(x+ "is stored in x.")
# # predicting
# # a
# x, y = 10, 2.5
# print(x+y)
# # it gives the sum of 12.5 meaning it added 10 and 2.5, it considers x to be 10 and y to be 2.5
# print(x/y)
# # gives an answer of 4.0
# print("Difference of x and y is:", x-y)
# # difference is 7.5
# # print("x*y=:"+ x*y)
# # gives an error because the outcome of x*y gives an int and int cannot be concatenated.
# # print(x+ "is stored in x.")
# # int cannot sum with a string.
#
# # ------------ ex3 ----------
# # 3. Write a python program to calculate the area of a circle.
# # Your program should accept the radius from a user.
# # You can assume that the user provides valid inputs only.
print('----------------- calculating Area of Circle-----------------')
user = int(input('enter the raduis of the circle of ur choice, preferably a number: '))
pie = 3.14
area = pie * (user**2)
print('the area of your circle is:', area)
