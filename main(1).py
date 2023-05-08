def longest_consecutive_path(matrix, start_char):
    def dfs(i, j, curr_len):
        nonlocal longest_len
        longest_len = max(longest_len, curr_len)
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < rows and 0 <= nj < cols and visited[ni][nj] == False and matrix[ni][nj] == curr_char + 1:
                visited[ni][nj] = True
                dfs(ni, nj, curr_len + 1)
                visited[ni][nj] = False
                
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    longest_len = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == start_char:
                curr_char = ord(start_char)
                visited[i][j] = True
                dfs(i, j, 1)
                visited[i][j] = False
    return longest_len
        

input_rows = 5
input_matrix = [
    ['D', 'E', 'H', 'X', 'B'],
    ['A', 'O', 'G', 'P', 'E'],
    ['D', 'D', 'C', 'F', 'D'],
    ['E', 'B', 'E', 'A', 'S'],
    ['C', 'D', 'Y', 'E', 'N']
]
start_char = 'C'

result = longest_consecutive_path(input_matrix, start_char)
print(f"The length of the longest path with consecutive characters starting from character {start_char} is {result}")
