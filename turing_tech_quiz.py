def calPoints(ops: list) -> int:
  """
  -An integer x, record a new score of x.
  -"+" record a new score that is the sum of the previous two scores.
  -"D" record a new score that is double the previous score.
  -"C" invalidate the previous score, removing it from the record.
  """  

  result = 0
  count = 0
  stack = list()

  for i in range(0, len(ops)):    
    print(stack)
    if ops[i] == "+":
      try:
        stack.append(int(stack[i - 3] + stack[i - 4]))
      except:
        continue

    elif ops[i] == "C":
      stack.pop()
    elif ops[i] == "D":
      stack.append(int(ops[i - 3] * 2))
    else:
      stack.append(int(ops[i])) 
      
    print(stack) 
  
  for j in stack:
    try:
      j == int(j)
      result += j
    except:
      continue

  return result

ops = [5, -2, 4, "C", "D", 9, "+", "+"]
calPoints(ops)