'''
UACC 1 P4 - Converging Streams
https://dmoj.ca/problem/uacc1p4
10pt

Type: Dynamic Programming, Graph Theory
>easy 10pt,DP, Graph, topological sort,branch and junction of streams,averaged, weighted proportion polution 
similar:

Key point:
Note:
- voted for 10pt, initially 7pt
v01
submit 2024-01-10
WA
"pollution values from each stream are averaged,
weighted proportionally based on the volume of water in each stream,
before pi is added to the pollution value."
v02
- add volume of water
- keep multiples of vol*polution
- divide by total vol at the junction when its indegree becomes 0 
submit 2024-01-11

'''
import sys
input = sys.stdin.readline

def topological_sort_BFS(g, in_deg, addings):
   q = [] # list/stack of vertices with 0 indegrees
   s = [] # ordered sequence
   sub = [(0,0) for i in range(len(g))]
   mul = [0]*len(g)
   for v in range(len(in_deg)):
      if in_deg[v] == 0: # "expect only one overall source"
         q.append(v)
         # water initial volumn as 1, polution = 0 + adding
         vol = 1
         pol = 0+addings[v]
         sub[v] = (vol, pol)
         mul[v] = vol * pol
   while len(q):
      v = q.pop()
      s.append(v)
      v_vol, v_pol = sub[v]
      #vol_v = volume[v]
      for a, f in g[v]:
         in_deg[a] -= 1
         a_vol, a_pol = sub[a] 
         sub[a] = (a_vol + v_vol*f/100, a_pol) #a_pol is not meaningful now
         mul[a] += (v_vol * f / 100) * v_pol
         if in_deg[a] == 0:
            q.append(a)
            a_vol, a_pol = sub[a]
            a_pol = mul[a] / a_vol + addings[a]
            sub[a] = (a_vol, a_pol)
   #print(s)
   return sub

N,M = map(int,input().split())
g      = [[] for i in range(N)]
in_deg = [0  for i in range(N)]
#src    = [[] for i in range(N)]
polution = []
for _ in range(M):
   u,v,f = map(int, input().split())
   u -= 1
   v -= 1
   g[u].append((v,f))
   in_deg[v] += 1
   #src[v].append((u,f))

polution = list(map(int, input().split()))

sub = topological_sort_BFS(g, in_deg, polution)
for vol, pol in sub:
   print(pol)

'''
Sample Input 1
3
1
2
1

Sample Output
2
============================
my Sample Input 2
27
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
100000

Sample Output 2
7
=========================
my Sample Input
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393

my Output for Sample Input
2 3 5 7 11 13 17 19 23 29 
31 37 41 43 47 

'''

