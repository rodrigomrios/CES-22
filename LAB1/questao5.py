def is_palindrome(s):
    
    p = s[::-1]
    
    if p == s:
        return True
    
    else:
        return False
    
    return False

print(is_palindrome('arara'))
print(is_palindrome('palindromo'))