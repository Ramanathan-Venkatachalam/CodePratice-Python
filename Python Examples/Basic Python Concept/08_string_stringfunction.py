"""
String and String Functions
"""
a= "rahul drasid"
print(a)
print(a.upper())
print(a.lower())

print(a.capitalize())
print(a.title())

print(a.count("r"))
print(a.endswith("id"))
print(a.find("a"))
print(a.find("r", 5))
print(a.replace("s","v"))

b= "sachin100"
print(b.isupper())
print(b.islower())
print(b.isalnum())
print(b.isalpha())

c = "he\nis\ngood"
print(c.splitlines())
print(c.splitlines(True))

d = "Rahul is new coach"
print(d.split())

e = "     Hello    "
print(len(e))
print(len(e.strip()))
print(len(e.lstrip()))
print(len(e.rstrip()))

date= "12-12-2021"
print(date.partition("-"))


