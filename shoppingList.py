numberOfItems = int(input("Enter number of items:\n"))
items = []
readLines = []
for x in range (numberOfItems):
    items.append(str(input("Give me the " + str(x+1) + ". item of " + str(numberOfItems) + "\n")))

with open("output.txt","w") as output:
    for item in items:
	    output.write(item + "\n")
		
with open("output.txt","r") as input:
    temporaryReadLines = input.readlines()

for thing in temporaryReadLines:
    readLines.append(thing.strip())

print("\n")
	
for item in readLines:
    print (item)