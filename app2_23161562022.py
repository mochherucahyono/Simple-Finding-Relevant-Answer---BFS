from collections import deque

def bfs_route(graph, start, goal):
    queue = deque([(start, [start])]) 
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        
        if node == goal:
            return path  
        
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None  

def bfs_faq(graph, query):
    queue = deque([query])
    visited = set()
    
    while queue:
        node = queue.popleft()
        
        if node in graph.get("answers", {}):
            return graph["answers"][node] 
        
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
    
    return "No relevant answer found."

faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}

query = "What is AI?"
answer = bfs_faq(faq_graph, query)
print("Relevant Answer:", answer)