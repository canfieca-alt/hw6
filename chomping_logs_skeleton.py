import numpy as np
from sys import argv

# Usage (run from the command line): python chomping_logs.py <file_containing_V_data> <LF> <LM>

"""
Examples:
python chomping_logs.py test22.txt 2 2
20
python chomping_logs.py test22.txt 2 0
6
python chomping_logs.py test22.txt 0 2
10
"""

"""
Computes the maximum amount of revenue achievable by chomping a fir log of length LF and maple log of length LM into bundles,
with prices according to V.

Parameters:
    V: The log bundle value input matrix.
    LF: The length of the input fir log.
    LM: The lenfth of the input maple log.

Returns:
    The maximum amount of revenue achievable by chomping a fir log of length LF and maple log of length LM into bundles.
"""
def log_values(V, LF, LM):
    # TODO: Implement this function and set its return value correctly!
    # Hint: The command np.zeroes((x, y), "int") returns an x-by-y matrix initialized to all zeroes.

    m = len(V) - 1
    n = len(V[0]) - 1

    dp = [[[0 for _ in range(n + 1)] for _ in range(LM + 1)] for _ in range(LF + 1)]

    # Fill the dp array using bottom-up dynamic programming             
    for i in range(LF + 1):
        for j in range(LM + 1):
            for k in range(min(i, m) + 1):
                dp[i][j][k] = max(
                    dp[i][j][k],
                    dp[i - k][j][k - 1] + V[k][0],
                    dp[i][j - k][k - 1] + V[0][k],
                )

                if k > 0:
                    for l in range(1, min(k, j) + 1):
                        dp[i][j][k] = max(
                            dp[i][j][k],
                            dp[i - l][j - k][l - 1] + V[k][l],
                            dp[i - k][j - l][l - 1] + V[l][k],
                            dp[i - l][j][l - 1] + V[k][0],
                            dp[i][j - l][l - 1] + V[0][l],
                        )

    return dp[LF][LM][min(LF, m)]

def read_V_from_file(file_name):
    VL = []
    f = open(file_name, "r")
    for line in f:
        VL += [[int(num) for num in line.strip().split()]]
    f.close()
    return np.array(VL)

file_name = argv[1]
V = read_V_from_file(file_name)
LF = int(argv[2])
LM = int(argv[3])

# Uncomment the following line to check how the input matrix V was parsed.
print(V)

print(log_values(V, LF, LM))