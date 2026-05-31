def check_gas_supply(cities, storages, pipelines):
    graph = {node: [] for node in (cities + storages)}
    for start, end in pipelines:
        if start in graph:
            graph[start].append(end)
    
    final_result = []

    for storage in storages:
        visited = set()
        stack = [storage]
        
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for neighbor in graph.get(current, []):
                    stack.append(neighbor)
        
        unreachable = [city for city in cities if city not in visited]
        
        if unreachable:
            final_result.append([storage, unreachable])
            
    return final_result