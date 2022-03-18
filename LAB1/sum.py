def sum_to(n):
  
      s = 0
      
      for i in range(n+1):
            
            s = s + i
      
      return s

s = sum_to(100)
print("A soma é:")
print(s)