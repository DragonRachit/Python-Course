import csv

with open("practice.csv", 'w', newline="") as f:
    head=["Name", "Age"]
    writer=csv.DictWriter(f, fieldnames=head)
    writer.writeheader()
    writer.writerow({"Name": "Ram", "Age": 12})
    writer.writerow({"Name": "Shyam", "Age": 12})
