def compress_string(s):
  res=""
  i=0
  while i<len(s):
    res+=s[i]
    count=1
    while i+1<len(s) and s[i]==s[i+1]:
      count+=1
      i+=1
    if count>1 or count==1:
      res+=str(count)
    i+=1

  return res

s=input('Enter the string: ')
ans=compress_string(s)
print(ans)