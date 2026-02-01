import math
def cannot(x):
    if x == 1: 
        return False
    elif x == 2:
        return True
        
    elif x % 2 ==0:
        return False
        
    numbers = list(range(3,int(math.sqrt(x))+1,2))
    for i in numbers:
        if x%i == 0:
            return False
    return True

number = cannot(int(input()))   
print(number)
