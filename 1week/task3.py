
def areDifferent(char1: chr, char2: chr) -> int:
    if char1 != char2:
        return 1
    else:
        return 0

def minDistance(word1: str, word2: str) -> int:
    init_value = max(len(word1), len(word2)) + 1
    matrix = [[init_value for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        matrix[i][0] = i
    for i in range(len(word2) + 1):
        matrix[0][i] = i
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            matrix[i][j] = min(
                matrix[i][j-1] + 1,
                matrix[i-1][j] + 1,
                matrix[i-1][j-1] + areDifferent(word1[i-1], word2[j-1])
            )
    return matrix[len(word1)][len(word2)]

def main():
    print("Enter str1:")
    s1 = input()
    print("Enter str2:")
    s2 = input()
    print(minDistance(s1, s2))

main()
