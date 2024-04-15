# The difference between res.append(subset) and res.append(list(subset)) is
# that the former appends the reference to the original subset list to res, 
# while the latter appends a new list object created from the elements of subset.

# When you append subset to res, you are appending a reference to the original
# subset list object. This means that if you modify subset after appending it to res, 
# the modification will also be reflected in res. For example:

subset = [1, 2, 3]
res = []
res.append(subset)

subset.append(4)
print(res)  # Output: [[1, 2, 3, 4]]


# On the other hand, when you append list(subset) to res, you are creating a new 
# list object from the elements of subset. This means that any modifications you
# make to subset after appending list(subset) to res will not affect res. 
# For example:


subset = [1, 2, 3]
res = []
res.append(list(subset))

subset.append(4)
print(res)  # Output: [[1, 2, 3]]
