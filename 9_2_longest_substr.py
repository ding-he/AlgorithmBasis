# 最长公共子串
def longest_substr(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    cell =[[0 for _ in range(len2)] for _ in range(len1)]

    maxlen = 0
    indexi = 0
    indexj = 0
    for i, s1 in enumerate(str1):
        for j, s2 in enumerate(str2):
            if s1 == s2:
                if i == 0 or j == 0:
                    cell[i][j] = 1
                else:
                    cell[i][j] = cell[i - 1][j - 1] + 1
            else:
                cell[i][j] = 0

            if maxlen < cell[i][j]:
                maxlen = cell[i][j]
                indexi = i
                indexj = j

    return str1[indexi + 1 - maxlen:indexi + 1], maxlen



# 最长公共子序列
def longest_subseq(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    cell = [[0 for _ in range(len2)] for _ in range(len1)]

    maxlen = 0
    for i, s1 in enumerate(str1):
        for j, s2 in enumerate(str2):
            if s1 == s2:
                if i == 0 or j == 0:
                    cell[i][j] = 1
                else:
                    cell[i][j] = cell[i - 1][j - 1] + 1
            else:
                if i == 0 and j == 0:
                    cell[i][j] = 0
                elif i != 0 and j == 0:
                    cell[i][j] = cell[i - 1][j]
                elif i == 0 and j != 0:
                    cell[i][j] = cell[i][j - 1]
                else:
                    cell[i][j] = max(cell[i - 1][j], cell[i][j - 1])

            if maxlen < cell[i][j]:
                maxlen = cell[i][j]

    print(cell)
    return maxlen


print(longest_substr('fish', 'fosh'))
print(longest_subseq('fish', 'fosh'))
