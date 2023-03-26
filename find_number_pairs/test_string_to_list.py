string1= "[10, 20, 30, 40],50  "

string1 = string1.strip()
string1 = string1.replace("[","")
string1 = string1.replace("]","")
string1=list(map(int, string1.split(",")))
print(string1)