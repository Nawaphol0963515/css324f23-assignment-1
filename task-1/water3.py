
def initial_state():
    return (8, 0, 0)  # (8-liter bottle, 5-liter bottle, 3-liter bottle)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    # pour from one to another

    # pour to x
    total = 8 - x
    if y>0 and total>0:
      if y>total:
        yield ((8, y-total, z), total)
      else :
        yield ((x+y, 0, z), y)
    if z > 0 and total>0:
      if z>total:
        yield ((8, y, z-total), total)
      else :
        yield ((x+z, y, 0), z)
    
    # pour to y
    total = 5 - y
    if x>0 and total>0:
      if x>total:
        yield ((x-total, 5, z), total)
      else:
        yield ((0, y+x, z), x)
    if z>0 and total>0:
      if z>total:
        yield ((x, 5, z-total), total)
      else:
        yield ((x, y+z, 0), z)

     # pour to z
    total = 3 - z
    if x>0 and total>0:
     if x>total:
      yield ((x-total, y, 3), total)
     else:
      yield ((0, y, z+x), x)
    if y>0 and total>0:
     if y>total:
      yield ((x, y-total, 3), total)
     else:
      yield ((x, 0, z+y), y)
