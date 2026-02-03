def isPrime(x):
    if x <= 1:
      return False
    elif x == 2:
      return True
    elif x%2 == 0:
      return False
        
    i = 3
    while i*i <= x:
        if x%i == 0:
            return False
        i += 2
    return True
    
num = isPrime(int(input()))  
print(num)
