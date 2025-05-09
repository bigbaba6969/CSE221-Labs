import sys
 
def find_first_one():
    
    T = int(sys.stdin.readline().strip())
 
    results = []
    for _ in range(T):
        S = sys.stdin.readline().strip()
        
        
        index = S.find('1')
 
        
        results.append(str(index + 1 if index != -1 else -1))
    
    
    sys.stdout.write("\n".join(results) + "\n")
 
 
if __name__ == "__main__":
    find_first_one()