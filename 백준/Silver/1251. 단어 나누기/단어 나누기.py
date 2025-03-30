word = input().strip()

n = len(word)
result = []

for i in range(1, n):
    for j in range(i + 1, n):
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        reversedFirst = first[::-1]
        reversedSecond = second[::-1]
        reversedThird = third[::-1]

        resultWord = reversedFirst + reversedSecond + reversedThird
        result.append(resultWord)

print(min(result))
