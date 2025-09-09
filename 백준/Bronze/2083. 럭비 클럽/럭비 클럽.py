import sys

def classify_rugby_player(age, weight):
  if age > 17 or weight >= 80:
    return "Senior"
  else:
    return "Junior"

if __name__ == "__main__":
  for line in sys.stdin:
    parts = line.split()
    if parts[0] == '#' and parts[1] == '0' and parts[2] == '0':
      break
    
    name = parts[0]
    age = int(parts[1])
    weight = int(parts[2])

    classification = classify_rugby_player(age, weight)
    print(f"{name} {classification}")