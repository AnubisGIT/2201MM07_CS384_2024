def sum(n):
  while n>=10:
    sum=0
    while n>0:
      r=n%10
      sum=sum+r
      n=n//10
    n=sum
    print(n)
  return n

num=input('Enter a Number: ')
num=int(num)
print(sum(num))