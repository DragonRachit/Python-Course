import csv

with open("practice.csv", 'w') as f:
    head=["Name", "Age"]
    writer=csv.DictWriter(f, fieldnames=head)
    writer.writeheader()
    

