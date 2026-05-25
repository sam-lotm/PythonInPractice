people = ["jack", "dan", "lorry"]

for i in range(len(people)):
    print(people[i])

Cars = [
    {"brand": "Ford", "model": "Mustang", "year": 1964},
    {"brand": "Porsche", "model": "911", "year": 1969},
    {"brand": "Honda", "model": "NSX", "year": 1991}
    ]
for car in Cars:
    print(car["brand"], car["model"], car["year"])

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
  
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

with open("demofile.txt") as f:
  for x in f:
    print(x)