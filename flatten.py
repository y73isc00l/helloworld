def checkdeflation(lst):
  for elem in lst:
    if isinstance(elem,list): return False
  return True

def my_flatten(lst):
  if checkdeflation(lst)==True:return lst
  else:
    count=len(lst)
    for i in range(count):
      temp=lst[-1]
      temp1=[]
      del lst[-1]
      if isinstance(temp,(int,float,str)):
          temp1.append(temp)
          lst.extend(temp1)
      else: lst.extend(temp)
    return my_flatten(lst)

