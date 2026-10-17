# Fibbonachi Series

def Fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return Fib(n-1)+Fib(n-2)
    
for i in range(7):
    print(Fib(i))
    
# Exponent

def power(x, y):
    print("Calling power(", x, ", 1) =", x)
    
    if y==1: #Base case
        print("Base case reached: power(", x, ", 1) =", x)
        return x
    else:
        half = power(x, y // 2)
        
        if y % 2 == 0:
            result = half*half
            print("Returning", result, "for power(", x, ",", y, ")")
            return result
        else:
            result = x * half * half
            print("Returning", result, "for power(", x, ",", y, ")")
            return result
print("Final Answer:", power(3,5))

# Countdown

def countdown(n):
    if n <= 0:
        print("Blast off!")
        return
    
    print(n)
    countdown(n-1)
    
countdown(5)

# Palindrome

def is_palindrome(word):
    if len(word) <= 1:
        return str(True) + " Palindrome"
    
    if word[0] != word[-1]:
        return str(False) + " Palindrome"
    return is_palindrome(word[1:-1])

print(is_palindrome("hello") ,"\n", is_palindrome("level"))

# String Reverse

def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])
print(reverse_string("Python"))

# Countup

def countup(n, start=0):
    if n != start:
        start += 1
        print(start)
        countup(n, start)
    else:
        print("Blast off!")

countup(5)