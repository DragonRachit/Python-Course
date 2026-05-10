sentence={}
sen=input("Enter your senetence: \n")
x=sen.strip("?,!.")
x=sen.split()

for i in x:
    if i in sentence:
        sentence[i]+=1
    else:
        sentence[i]=1

print(sentence)