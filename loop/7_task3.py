data=[1,2,3,'hi','hello',5,6,7]
total=0
for each in data:
  if not type(each)==int:
      continue
  total+=each
        
print(total)

        
