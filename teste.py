dimensions = (200, 50)
print(id(dimensions))
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
 
dimensions = (400, 100)
print(id(dimensions))
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

