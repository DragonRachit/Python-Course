# f= open("Hello.txt")
# print(f.read())
# f.close()


# with open("Hello.txt",'a') as f:
#     f.write("\nWelcome to python")

# with open("Hello.txt") as f:
#     x=f.readline()
#     print(x)

# CSV file

# import csv

# with open("data.csv", 'w', newline='') as csvfile:
#     writer=csv.writer(csvfile)
#     writer.writerow(["Name", "Age"])
#     writer.writerow(["Rachit", 12])
#     writer.writerows([["G17", 99],["R23", 200]])



# import csv

# with open("data.csv", "w",  newline="") as f:
#     w=["Name", "Age"]
#     writer=csv.DictWriter(f, fieldnames=w)
#     writer.writeheader()
#     writer.writerow({"Name":"Ram", "Age": 12})
#     writer.writerow({"Name":"Hari", "Age": 21})