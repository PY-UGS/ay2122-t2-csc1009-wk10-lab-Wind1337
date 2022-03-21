modCode = input("Input module code: ")

match(modCode):
    case "CSC1006":
        print("Mathematics 2")
    case "CSC1007":
        print("Operating Systems")
    case "CSC1008":
        print("Data Structure and Algorithms")
    case "CSC1009":
        print("Object Oriented Programming")
    case "CSC1010":
        print("Computer Networks")

for i in range(102, 66, -1):
    if (i % 2) != 0:
        print(i)
