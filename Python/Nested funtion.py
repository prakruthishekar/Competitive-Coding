def outer_function():
    x = 1
    
    def inner_function():
        print(x)
        x +=1
        print(x)
        
    inner_function()

outer_function()  # prints 1


    # This code will raise an UnboundLocalError with the message "local variable 'x' 
    # referenced before assignment".

    # In Python, when you try to modify a variable that is defined outside of the 
    # inner function's scope, Python considers that variable to be a "local variable"
    # within the inner function's scope. This means that you can read the value of the
    # variable, but you cannot modify it unless you declare it as a non-local variable 
    # using the nonlocal keyword.

    # Here's an updated version of the code that uses the nonlocal keyword to declare 
    # x as a non-local variable:


def outer_function():
    x = 1
    
    def inner_function():
        nonlocal x
        print(x)
        x += 1
        print(x)
        
    inner_function()

outer_function()  # prints 1, then 2
