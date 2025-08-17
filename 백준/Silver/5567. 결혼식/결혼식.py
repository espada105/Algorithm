n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

friends = set(graph[1])

friends_of_friends = set()
for friend in friends:
    friends_of_friends.update(graph[friend])

invited = friends | friends_of_friends
invited.discard(1)

print(len(invited))