# 2410. Maximum Matching of Players With Trainers

## Problem Description

You are given two 0-indexed integer arrays:
- `players`: `players[i]` is the ability of the $i^{th}$ player.
- `trainers`: `trainers[j]` is the training capacity of the $j^{th}$ trainer.

A player can match with a trainer if `players[i] <= trainers[j]`. Each player and trainer can be matched at most once. The goal is to return the **maximum number of matchings**.

## Greedy Strategy

This problem is a classic application of the **Greedy Algorithm**, specifically the "Smallest to Smallest" matching strategy.

### Logic
1.  **Sort both arrays**: By sorting both `players` and `trainers`, we can process them in increasing order of ability and capacity.
2.  **Greedy Choice**: To maximize matchings, we want to satisfy the players with the smallest abilities using the trainers with the smallest possible capacities that are still $\geq$ the player's ability.
    - If we use a very powerful trainer to satisfy a weak player, we might "waste" that trainer's capacity when a more powerful player comes along.
    - If a trainer cannot satisfy the current weakest player, that trainer cannot satisfy any subsequent (stronger) players, so we move to the next trainer.

## Implementation Details

The initial implementation used a `while` loop with two pointers. We can optimize this slightly for readability and efficiency in Python.

### Original Implementation
```python
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        i, j = 0, 0 
        while i < m and j < n:
            if players[i] <= trainers[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i
```

### Optimized Implementation
The optimization simplifies the loop by iterating directly over the `trainers` and advancing the `player_idx` only when a match is found.

```python
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        player_idx = 0
        m = len(players)
        
        for trainer_capacity in trainers:
            if player_idx < m and players[player_idx] <= trainer_capacity:
                player_idx += 1
                
        return player_idx
```

## Complexity Analysis

- **Time Complexity**: $O(P \log P + T \log T)$, where $P$ is the number of players and $T$ is the number of trainers. This is dominated by the sorting step. The matching loop itself is $O(P + T)$.
- **Space Complexity**: $O(1)$ or $O(P + T)$ depending on the space used by the sorting algorithm implementation (Python's Timsort uses $O(P + T)$ auxiliary space).
