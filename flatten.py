#!/usr/bin/python2
def my_flatten(lst):
  count=len(lst)
  for i in range(count):
    elem=lst[0]
    del lst[0]
    if not isinstance(elem,list):
      yield elem
    else:
      for childelem in my_flatten(elem):
        yield childelem

