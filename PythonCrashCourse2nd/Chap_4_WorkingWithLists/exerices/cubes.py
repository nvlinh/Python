#Normal way
cubes = []
for number in range(1,11):
	cubes.append(number**3)

for cube in cubes:
	print(cube)

#Comperhension way
for cube in [number**3 for number in range(1,11)]:
	print(cube)