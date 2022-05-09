name = "Ramu Venkat"
print(type(name))

para = """ Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. """
print(type(para))
print(para)

#Getting Multiline String as input
para=["21","22","23"]
print(type(para))
print(','.join(para))

para=[]
print(type(para))
print("Enter the para: ")

while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)
output= '\n'.join(para)
print(output)