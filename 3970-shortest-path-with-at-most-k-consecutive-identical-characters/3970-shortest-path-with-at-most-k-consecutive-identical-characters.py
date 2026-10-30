import heapq
from typing import List


class Solution:

  def shortestPath(
      self, n: int, edges: List[List[int]], labels: str, k: int
  ) -> int:
    if n == 1:
      return 0

    adj = [[] for _ in range(n)]
    for u, v, w in edges:
      adj[u].append((v, w))

    k1 = k + 1
    dist = [float("inf")] * (n * k1)
    dist[0 * k1 + 1] = 0
    pq = [(0, 0, 1)] 

    while pq:
      d, u, count = heapq.heappop(pq)

      if u == n - 1:
        return d

      if d > dist[u * k1 + count]:
        continue

      u_label = labels[u]

      for v, w in adj[u]:
        nxt_count = count + 1 if labels[v] == u_label else 1
        if nxt_count > k:
          continue

        nxt_idx = v * k1 + nxt_count
        nxt_d = d + w

        if nxt_d < dist[nxt_idx]:
          dist[nxt_idx] = nxt_d
          heapq.heappush(pq, (nxt_d, v, nxt_count))

    return -1