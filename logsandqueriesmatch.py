"""
Queries and Logs Matching Problem

Design a QueriesSearchObject that processes input strings in two formats:
1. "Q:helloworld" - represents a query with content "helloworld"
2. "L:hellomorningworld" - represents a log with content "hellomorningworld"

Requirements:
- Each query is assigned a unique query ID when processed
- When processing a log, return all query IDs that match the log
- A query matches a log if ALL words in the query appear in the log
- Word matching can be either:
  - Simple presence: word just needs to appear in log
  - Count-based: log must contain >= count of each word as in query

Solution approach:
- Use inverted index to track which queries contain each word
- When processing logs, use the inverted index to find candidate queries
- Verify each candidate by checking if all query words appear in the log
"""

from collections import defaultdict, Counter
from typing import List, Set, Dict


class QueriesSearchObject:
    def __init__(self, count_based_matching=True):
        """
        Initialize the search object.
        
        Args:
            count_based_matching (bool): If True, requires exact word count matching.
                                       If False, only requires word presence.
        """
        self.count_based_matching = count_based_matching
        self.query_id_counter = 0
        self.queries = {}  # query_id -> query_content
        self.query_word_counts = {}  # query_id -> Counter of words
        self.inverted_index = defaultdict(set)  # word -> set of query_ids
        
    def process_line(self, line: str) -> List[int]:
        """
        Process a single line input.
        
        Args:
            line (str): Input line in format "Q:content" or "L:content"
            
        Returns:
            List[int]: For queries, returns empty list. 
                      For logs, returns list of matching query IDs.
        """
        if not line or ':' not in line:
            return []
            
        prefix, content = line.split(':', 1)
        
        if prefix == 'Q':
            return self._process_query(content)
        elif prefix == 'L':
            return self._process_log(content)
        else:
            return []
    
    def _process_query(self, query_content: str) -> List[int]:
        """Process a query and store it with assigned ID."""
        query_id = self.query_id_counter
        self.query_id_counter += 1
        
        # Store query
        self.queries[query_id] = query_content
        
        # Extract words and count them
        words = query_content.lower().split()
        word_counts = Counter(words)
        self.query_word_counts[query_id] = word_counts
        
        # Update inverted index
        for word in word_counts:
            self.inverted_index[word].add(query_id)
        
        print(f"Stored query {query_id}: '{query_content}'")
        return []
    
    def _process_log(self, log_content: str) -> List[int]:
        """Process a log and return matching query IDs."""
        log_words = log_content.lower().split()
        log_word_counts = Counter(log_words)
        
        # Find candidate query IDs using inverted index
        candidate_queries = set()
        for word in log_word_counts:
            if word in self.inverted_index:
                candidate_queries.update(self.inverted_index[word])
        
        # Check each candidate query for complete match
        matching_queries = []
        for query_id in candidate_queries:
            if self._query_matches_log(query_id, log_word_counts):
                matching_queries.append(query_id)
        
        matching_queries.sort()  # Return in sorted order
        print(f"Log '{log_content}' matches queries: {matching_queries}")
        return matching_queries
    
    def _query_matches_log(self, query_id: int, log_word_counts: Counter) -> bool:
        """Check if a query completely matches the log."""
        query_word_counts = self.query_word_counts[query_id]
        
        for word, query_count in query_word_counts.items():
            log_count = log_word_counts.get(word, 0)
            
            if self.count_based_matching:
                # Require log to have >= query count for each word
                if log_count < query_count:
                    return False
            else:
                # Only require word presence
                if log_count == 0:
                    return False
        
        return True
    
    def get_query_info(self, query_id: int) -> str:
        """Get query content by ID."""
        return self.queries.get(query_id, "Query not found")


def test_queries_search_object():
    """Test the QueriesSearchObject with various examples."""
    print("=== Testing Count-Based Matching ===")
    search_obj = QueriesSearchObject(count_based_matching=True)
    
    # Test queries
    test_inputs = [
        "Q:hello world",
        "Q:world hello",
        "Q:hello hello world",
        "Q:python programming",
        "L:hello world morning",
        "L:world hello hello programming",
        "L:hello world hello world",
        "L:python is great for programming",
        "L:morning world"
    ]
    
    for line in test_inputs:
        result = search_obj.process_line(line)
        if line.startswith('L:'):
            print(f"  -> Matching queries: {result}")
    
    print("\n=== Testing Presence-Only Matching ===")
    search_obj2 = QueriesSearchObject(count_based_matching=False)
    
    for line in test_inputs:
        result = search_obj2.process_line(line)
        if line.startswith('L:'):
            print(f"  -> Matching queries: {result}")


if __name__ == "__main__":
    test_queries_search_object()