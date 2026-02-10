def isPrime(x):
  if x == 2:
    return True
  elif x <= 1 or x%2 == 0:
    return Falsei 
  i = 3
  while i*i <= x:
    if x%i == 0:
      return False
    i += 2
    return True
    
num = isPrime(int(input()))  
print(num)
