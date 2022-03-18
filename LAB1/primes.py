import math

def is_prime(n):
      
      p = math.floor(math.sqrt(n))
      t = 0
      
      for i in range(p):
          
          if n % (i+1) == 0:
              t = t + 1
      
      if t == 1:
          
          return True
      
      else:
          
          return False
          
      return False


print(is_prime(458))