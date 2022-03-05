'''
BFS 너비우선탐색 : 시작점인 루트노드와 같은 거리에 있는 노드를 우선으로 방문,
보통 큐 자료구조 이용, 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보만
큐에 넣어 먼저 큐에 들어있던 노드부터 방문

DFS 깊이우선탐색 : 갈 수 있는 끝까지 탐색해 리프노드를 방문하고, 이전 갈림길에서 
선택하지 않았던 노드를 방문, 보통 스택 자료구조 이용하거나 재귀이용, 먼저 방문한 노드에 연결된 노드보다
현재 방문한 노드에 연결된 노드를 방문

https://www.acmicpc.net/problem/11725
트리의 부모 찾기
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
visited = [False] * (n+1)
answer = [0] * (n+1)

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs():
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for i in tree[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                answer[i] = node

bfs()

for i in answer[2:]:
    print(i)


# DFS 풀이(1. 스택사용)
# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# visited = [False] * (n+1)
# answer = [0] * (n+1)

# graph = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# def dfs():
#     stack = deque()
#     stack.append(1)
#     while stack:
#         node = stack.pop()
#         for i in graph[node]:
#             if not visited[i]:
#                 stack.append(i)
#                 visited[i] = True
#                 answer[i] = node

# dfs()
# for i in answer[2:]:
#     print(i)


# DFS풀이(2. 재귀)
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# n = int(input())
# visited = [False] * (n+1)
# answer = [0] * (n+1)
# tree = [[] for _ in range(n+1)]

# for _ in range(n-1):
#     a, b = map(int, input().split())
#     tree[a].append(b)
#     tree[b].append(a)

# def dfs(num):
#     visited[num]=True
#     for i in tree[num]:
#         if not visited[i]:
#             answer[i]=num
#             dfs(i)

# dfs(1)

# for i in answer[2:]:
#     print(i)