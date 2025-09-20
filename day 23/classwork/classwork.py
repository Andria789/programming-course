#upper  converts all letters to uppercase
#lower  converts all letters to lowercase
#capitalize  makes the first letter uppercase, the rest lowercase
#title  makes the first letter of every word uppercase
#find  searches for a  word in the string and returns the first word if there isnt the letter it returns -1
#count   counts how many times a  word or symbol appears in the string
test = ["andria", "anita"]

print("andria".upper())
print("andria".lower())
print("andria".capitalize())
print("andria".title())
print("test".find("a"))
print("test".count("n"))


print(len("test"))#counts the amount of indexes in a string or a list
test.append("ioane")#adds a element at the end of the list
test.insert(2, False)
test.pop(-1)
test.remove("andria")#removes a element out of the list or string
