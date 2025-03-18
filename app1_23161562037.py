from collections import deque

def shortest_path(city_map, start, end):
    queue = deque([(start, [start])])  # (current_node, path_so_far)
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in city_map.get(node, []):
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Return None if no path is found

# Contoh penggunaan
city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

start = 'Home'
end = 'Hospital'
print("Rute Terpendek:", shortest_path(city_map, start, end))
