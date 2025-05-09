import sys
import bisect
 
def process_queries():
    n, q = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort() 
 
    results = []
    for _ in range(q):
        x, y = map(int, sys.stdin.readline().split())
 
 
        left_index = bisect.bisect_left(arr, x)
        right_index = bisect.bisect_right(arr, y)
 
        count = right_index - left_index
        results.append(str(count))
 
    sys.stdout.write("\n".join(results) + "\n")
 
if __name__ == "__main__":
    process_queries()