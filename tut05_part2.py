def balanced_paranthesis(brackets):
  stack=[]
  for i in brackets:
    if i in ['(','{','[']:
      stack.append(i)
    else:
      if not stack:
        return False
      current_char=stack.pop()
      if current_char=='(':
        if i!=')':
          return False
      if current_char=='{':
        if i!='}':
          return False
      if current_char=='[':
        if i!=']':
          return False
  if stack:
    return False
  return True

brackets=input('Enter the brackets: ')
if balanced_paranthesis(brackets):
  print('The input string is balanced.')
else:
  print('The input string is NOT balanced.')