def isWellFormed(s):
  stack = []
  for bracket in s:
    if bracket == '[' or bracket == '(' or bracket == '{':
      stack.append(bracket)
    else:
      if not stack:
        print("INVALID") 
        return
      popped = stack.pop()

      if (popped == ']' and bracket != '[') or \
        (popped == ')' and bracket != '(') or \
        (popped == '}' and bracket != '{'):
        return
        print("INVALID")
  print("VALID")

isWellFormed("([])[]({})")