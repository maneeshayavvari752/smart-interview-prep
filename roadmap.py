TOPIC_GRAPH = {
    "Arrays": ["Prefix Sum", "Sliding Window", "Two Pointers"],
    "Strings": ["Pattern Matching", "String Hashing"],
    "Linked List": ["Fast Slow Pointer", "Reversal"],
    "Stack": ["Monotonic Stack", "Expression Evaluation"],
    "Queue": ["Deque", "Circular Queue"],
    "Trees": ["BST", "Tree Traversal", "Recursion"],
    "Graphs": ["BFS", "DFS", "Dijkstra"],
    "DP": ["Memoization", "Tabulation"]
}


def generate_roadmap(weak_topics):
    roadmap = []

    for topic in weak_topics:
        topic = topic.strip()

        if topic.lower() == "dp":
            topic = "DP"
        else:
            topic = topic.title()

        if topic in TOPIC_GRAPH:
            roadmap.append(topic)

            for subtopic in TOPIC_GRAPH[topic]:
                roadmap.append(subtopic)

    return roadmap