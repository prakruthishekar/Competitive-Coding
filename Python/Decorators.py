# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
#         return result
#     return wrapper

# @timer
# def my_function():
#     # Some time-consuming operation
#     time.sleep(2)
#     return 3

# print(my_function())






# def bold(func):
#     def wrapper(*args, **kwargs):
#         return "<b>" + func(*args, **kwargs) + "</b>"
#     return wrapper

# def italic(func):
#     def wrapper(*args, **kwargs):
#         return "<i>" + func(*args, **kwargs) + "</i>"
#     return wrapper

# @bold
# @italic
# def hello(name):
#     return f"Hello, {name}!"

# print(hello("Alice"))



# In this example, we define two decorator functions bold and italic,
# each of which wraps a given function's return value in HTML tags. 
# We then define a hello function that takes a name argument and returns 
# a greeting string.

# We use the @bold and @italic decorator syntax to apply both decorators 
# to the hello function. This causes the hello function to be wrapped with 
# the wrapper function returned by each decorator, effectively modifying its behavior.

# When we call the hello function with the argument "Alice", the wrapper
#  function returned by the italic decorator is executed first, which wraps
#  the result of the hello function call in <i> tags. The wrapper function 
#  returned by the bold decorator is then executed, which wraps the result of 
#  the previous call in <b> tags.

# The final result of the hello function call is the string "Hello, Alice!" 
# wrapped in both <i> and <b> tags, resulting in the HTML string <b><i>Hello,
# Alice!</i></b>. This string is then printed to the console using the print statement.

# Overall, this example shows how decorators can be used to modify the behavior
# of a function by wrapping its return value in additional code, without
# modifying its source code. This can be very useful for adding functionality 
# to existing functions in a modular and reusable way.




a1 = [1,2,3]
a2 = [6,5,3]

def find(l, n):
    for i in range(n-1,len(l),n):
        l[i] = l[i] ** 3
    return l


def nest(l):
    res = []
    for i in l:
        if type(i) == int:
            res.append(i)
        else:
            res.extend(nest(i))
    res.sort()
    return res

print(nest([1,[2,[3,4]]]))

    


def f(l, s):
    st = s.split()
    for i in l:
        if i[0] in s:
            i[1] = (i[1] * 110) / 100
    return l


print(f([['Sweet_Corn_Soup', 300.0], ['Cream_of_Tomato_Soup', 100.0], ['Bacon_and_Cheese', 150.0], ['Honey_Mustard', 230.0], ['Hot_Coffee', 50.0], ['Cold_Coffee', 50.0], ['Egg_Sandwiches', 130.0], ['Tacos', 400.0]], 'Hot_Coffee Cold_Coffee Tacos'))




def fizzBuzz( n: int):
        a = []

        for i in range(1,n + 1):
            if i/3 ==0 and i/5 ==0:
                a.append('FizzBuzz')
 
            elif i/3 == 0 :
                a.append('Fizz')
            elif i / 5 == 0:
                a.append('Buzz')
            else:
                a.append(str(i))

        return a

print(fizzBuzz(3))
print(3/3)