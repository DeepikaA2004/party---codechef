def can_host_party(N, X):
    if N <= X:
        return "YES"
    else:
        return "NO"

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read N and X for each test case
    N, X = map(int, input().split())
    
    # Check if Chef can host the party
    result = can_host_party(N, X)
    
    # Print the result
    print(result)
