# import my_modules

# result = my_modules.greet("Zaid")
# print (result)

# x = 3
# y = 4

# print (my_modules.add(x,y))
# print (my_modules.substract(x,y))
# print (my_modules.devide(x,y))

# try:
#     num = int (input("enter a number>"))
#     result = 10 / num
#     print (f"result: {result}")
# except ZeroDivisionError:
#     print("divide by zero not allowed")
# except ValueError:
#     print ("invalid input! enter a number")
# else:
#     print(f"division succsess: {result}")
# finally:
#     print("execution completed")

def check_age (age):
    if age < 18:
        raise ValueError("Age must be 18 and above")
    else:
        print("valid age")

try:
    check_age(19)
except ValueError as e:
    print(f"error: {e}")
