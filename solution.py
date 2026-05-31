import csv
from collections import deque, defaultdict
import os

def get_max_flow(farms, shops, roads):
    capacity = defaultdict(lambda: defaultdict(int))
    source = "SUPER_SOURCE"
    sink = "SUPER_SINK"
    
    for u, v, cap in roads:
        capacity[u][v] += int(cap)
    
    for f in farms:
        capacity[source][f] = float('inf')
        
    for s in shops:
        capacity[s][sink] = float('inf')

    def bfs(s, t, parent):
        visited = {s}
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in capacity[u]:
                if v not in visited and capacity[u][v] > 0:
                    parent[v] = u
                    visited.add(v)
                    if v == t: 
                        return True
                    queue.append(v)
        return False

    max_flow = 0
    parent = {}
    
    while bfs(source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        parent = {}
        
    return max_flow

def create_sample_csv():
    filename = 'roads.csv'
    if not os.path.exists(filename):
        content = [
            "F1, F2, F3\n",
            "S1, S2, S3, S4, S5\n",
            "F1, X1, 10\n",
            "F2, X1, 5\n",
            "F3, X2, 15\n",
            "X1, X2, 4\n",
            "X1, S1, 10\n",
            "X2, S2, 10\n",
            "X2, S3, 5\n",
            "S1, S4, 2\n",
            "S3, S5, 8\n"
        ]
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(content)
        print(f"Файл {filename} було створено автоматично.")


def main():
    try:
        with open('roads.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            farms = [x.strip() for x in next(reader)]
            shops = [x.strip() for x in next(reader)]
            
            roads = []
            for row in reader:
                if row and len(row) == 3:
                    roads.append((row[0].strip(), row[1].strip(), int(row[2].strip())))
            
            result = get_max_flow(farms, shops, roads)
            print(f"Максимальна кількість машин, які можна доставити: {result}")
            
    except FileNotFoundError:
        print("Помилка: Файл roads.csv не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    create_sample_csv()
    main()