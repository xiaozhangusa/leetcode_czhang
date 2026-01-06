from typing import List
from collections import deque
import sys
import os

# Add current directory to path so we can import Solution
sys.path.append(os.getcwd())
from 934_ShortestBridge import Solution

def test_case_1():
    sol = Solution()
    grid = [[0,0,0,1,1],[0,0,0,1,0],[0,0,0,1,1],[0,0,1,0,1],[0,0,1,1,0]]
    result = sol.shortestBridge(grid)
    expected = 1
    print(f"Test Case 1: Result {result}, Expected {expected}. {'SUCCESS' if result == expected else 'FAILURE'}")

def test_case_2():
    sol = Solution()
    grid = [[0,1],[1,0]]
    result = sol.shortestBridge(grid)
    expected = 1
    print(f"Test Case 2: Result {result}, Expected {expected}. {'SUCCESS' if result == expected else 'FAILURE'}")

def test_case_3():
    sol = Solution()
    grid = [[0,1,0],[0,0,0],[0,0,1]]
    result = sol.shortestBridge(grid)
    expected = 2
    print(f"Test Case 3: Result {result}, Expected {expected}. {'SUCCESS' if result == expected else 'FAILURE'}")

def test_case_4():
    sol = Solution()
    grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    result = sol.shortestBridge(grid)
    expected = 1
    print(f"Test Case 4: Result {result}, Expected {expected}. {'SUCCESS' if result == expected else 'FAILURE'}")

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
