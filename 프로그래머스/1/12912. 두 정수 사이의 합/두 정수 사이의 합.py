def solution(a, b):
    if a < b:
        return (a + b)*(((b-a)+1)/2)
    else:
        return (b + a)*(((a-b)+1)/2)