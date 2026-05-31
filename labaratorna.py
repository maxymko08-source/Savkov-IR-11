from collections import deque
import os

def count_islands_bfs(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    islands_count = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                islands_count += 1
                
                queue = deque([(r, c)])
                grid[r][c] = 0
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            queue.append((nr, nc))
                            
    return islands_count

def process_matrix_file(filename):
    if not os.path.exists(filename):
        return None
    
    matrix = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                row_data = line.strip()
                if row_data:
                    matrix.append([int(x) for x in row_data.replace(',', ' ').split()])
        
        return count_islands_bfs(matrix)
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None