set1=set()
r=int(input("Enter the limits"))
for i in range(0,r):
	set1.add(input("Enter the number"))
print(set1)
set2=set()
l=int(input("Enter the limits"))
for i in range(0,l):
	set2.add(input("Enter the number"))
print(set2)
while True:
	print("......Sets operations......")
	print("1.....size of bytes")
	print("2.....length of the set")
	print("3.....Adding new element")
	print("4.....POP")
	print("5.....intersection")
	print("6.....set difference")
	print("7.....symmetric difference")
	print("8.....checking of a element")
	print("9.....clearing of a set")
	print("10....union of a set")
	ch=int(input("Enter your choice"))
	if ch == 1:
		print("Size of the bytes")
		set1.__sizeof__()
	elif ch == 2:
		print("Length of the set")
		print(len(set1))
	elif ch == 3:
		print("Adding the new element")
		n=int(input("Enter the number to add"))
		print(set1.add(n))
	elif ch == 4:
		print("POP")
		print(set1.pop())
	elif ch == 5:
		print(set1.intersection(set2))
	elif ch == 6:
		print(set1-set2)
	elif ch == 7:
		print("Symmetric difference")
		a=set1^set2
		print(a)
	elif ch == 8:
		print("Check the elements")
		s=int(input("Enter searching element"))
		print("set1")
		set1__contains__(r)
	elif ch == 9:
		print("union of the set")
		print(set1.union(set2))
	elif ch == 10:
		print("clear the set")
		set2.clear()
	else:
		print("Invalid")
		exit()

