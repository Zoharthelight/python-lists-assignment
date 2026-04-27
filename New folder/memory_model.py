a = [1,2,3]
b = a

b[0] = 100

print(a)
print(b)

print(id(a))
print(id(b))

# Answers:
# Why did both lists change?
# Because b is not a copy, it is a reference to the same list as a.

# Why are ids same?
# Both variables point to the same memory location.

# What does this mean?
# Lists are mutable and Python uses references, so changes affect all variables pointing to the same object.