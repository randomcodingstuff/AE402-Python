answer=str(input("Enter Name, Age, Status, Type, or Gender! "))
me={
      'Name':'Cosmo',
      'Birthday':'0331',
      'Status':'Confused',
      'Type':'Asian',
      'Gender':'Male',
      }
for k,v in me.items():
    print(k,v)
for k in me.keys():
    print(k)