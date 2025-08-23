import sys
import heapq

input = sys.stdin.readline

def alien_dictionary(words):
    # Build graph and indegree
    graph = {chr(c): set() for c in range(ord('a'), ord('z')+1)}
    indegree = {chr(c): 0 for c in range(ord('a'), ord('z')+1)}
    
    letters_present = set()  # letters that appear in words
    for word in words:
        for c in word:
            letters_present.add(c)
    
    n = len(words)
    for i in range(n - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        # Check prefix invalid case
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return "-1"
        # Find first differing character
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break
    
    # Lexicographically smallest topological sort using min-heap
    heap = []
    for c in letters_present:
        if indegree[c] == 0:
            heapq.heappush(heap, c)
    
    result = []
    while heap:
        c = heapq.heappop(heap)
        result.append(c)
        for nei in graph[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                heapq.heappush(heap, nei)
    
    if len(result) != len(letters_present):
        return "-1"  # cycle detected
    
    return ''.join(result)


if __name__ == "__main__":
    N = int(input())
    words = [input().strip() for _ in range(N)]
    print(alien_dictionary(words))
