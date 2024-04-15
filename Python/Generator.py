def fibonacci_generator():
    n1=0
    n2=1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2
sequence= fibonacci_generator()
arr = []
for i in range(100):
    (arr.append(next(sequence)))

print(arr)
print(len(arr))

# Output
