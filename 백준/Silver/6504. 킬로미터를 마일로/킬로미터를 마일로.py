fib = [1, 2]
while fib[-1] < 25000:
    fib.append(fib[-1] + fib[-2])

def to_fibonacci_binary(n):
    bits = [0] * len(fib)
    
    for i in range(len(fib) - 1, -1, -1):
        if n >= fib[i]:
            bits[i] = 1
            n -= fib[i]
    
    for i in range(len(bits) - 1):
        if bits[i] == 1 and bits[i + 1] == 1:
            bits[i] = 0
            bits[i + 1] = 0
            if i + 2 < len(bits):
                bits[i + 2] = 1
            else:
                bits.append(1)
                fib.append(fib[-1] + fib[-2])
    
    return bits

def from_fibonacci_binary(bits):
    result = 0
    for i in range(len(bits)):
        if i < len(fib) and bits[i] == 1:
            result += fib[i]
    return result

t = int(input())
for _ in range(t):
    x = int(input())
    
    fib_binary = to_fibonacci_binary(x)
    
    shifted = fib_binary[1:]
    
    y = from_fibonacci_binary(shifted)
    
    print(y)