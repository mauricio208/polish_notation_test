symbols = ['+', '-', '*', '/']

def reinfix(i):
  if len(i) == 1:
    return i[0]
  if i[1] in symbols:
    value = i.pop()
    index = 1
  else:
    value = i[1]
    index = 2
  return 'int({}{}({}))'.format(value,i[0],reinfix(i[index:]))

def max_expression(i,v):
  try:
    expression = reinfix(i.split())
    if not v:
            return eval(expression)
    all_expressions = [expression]
    values = []
    for k,limits in v.items():
      updated_expressions = []
      for i in range(limits[0],limits[1]):
        for e in all_expressions:
          updated_expressions.append(e.replace(k,str(i)))
      all_expressions = updated_expressions
    return max(map(eval,all_expressions))
  except Exception:
    return None

