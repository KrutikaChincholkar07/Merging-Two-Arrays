n1 = int(input("Enter size of first array: "))
arr1 = []

print("Enter elements of first array:")
for i in range(n1):
    arr1.append(int(input()))

n2 = int(input("Enter size of second array: "))
arr2 = []

print("Enter elements of second array:")
for i in range(n2):
    arr2.append(int(input()))

merged = arr1 + arr2

print("Merged array:", merged)
