# Introduction to Computation and Programming Using Python - John V. Guttag

x = 9 + 2
+ 33
print(x) # prints 11

y = (9 + 2
+ 33)
print(y) # prints 44

z = 9 + 2 +\
+ 33
print(z) # prints 44


# prints the largest odd number, if none of them are odd - print the smallest value of the three
answer = min(x, y, z)
if x%2 != 0:
    answer = x
if y%2 != 0 and y > answer:
    answer = y
if z%2 != 0 and z > answer:
    answer = z
print(answer)


# sets x to the maximum of y and z
num_x = int(input("x: "))
num_y = int(input("y: "))
num_z = int(input("z: "))
num_x = num_y if num_y > num_z else num_z
print(num_x)