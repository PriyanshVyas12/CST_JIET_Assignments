# Find element that occurs once.
ls = []
n = int(input("Enter size of array:"))
print("Enter ", n, " elements:")
for i in range(n):
    ls.append(int(input()))
a = ls[0]
for i in range(1, n):
    a = a ^ ls[i]
print("Element that occurs once: ", a)
