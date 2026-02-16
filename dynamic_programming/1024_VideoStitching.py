from typing import List

# You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths.

# Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.

# We can cut these clips into segments freely.

# For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
# Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. If the task is impossible, return -1.

 

# Example 1:

# Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
# Output: 3
# Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
# Then, we can reconstruct the sporting event as follows:
# We cut [1,9] into segments [1,2] + [2,8] + [8,9].
# Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
# Example 2:

# Input: clips = [[0,1],[1,2]], time = 5
# Output: -1
# Explanation: We cannot cover [0,5] with only [0,1] and [1,2].
# Example 3:

# Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
# Output: 3
# Explanation: We can take clips [0,4], [4,7], and [6,9].
 

# Constraints:

# 1 <= clips.length <= 100
# 0 <= starti <= endi <= 100
# 1 <= time <= 100

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        """
        Intuition: Greedy "Furthest Reach" (Jump Game II pattern)
        At each point, we pick the clip that extends our coverage the furthest into the future.
        """
        # STEP 1: Preprocessing - The "Max Reach" Map
        # For every possible start time (0 to time), find the furthest we can go with ONE clip.
        max_reach_at = [0] * (time + 1)
        for start, end in clips:
            if start <= time:
                max_reach_at[start] = max(max_reach_at[start], end)
        
        # STEP 2: Greedy Traversal - The Relay Race
        # current_end: The furthest point currently covered
        # next_end: The furthest point we can reach using ONE more clip
        # count: Number of clips used
        current_end = 0
        next_end = 0
        count = 0
        
        # We traverse the timeline from 0 to time
        for i in range(time + 1):
            # Update the candidate furthest reach
            next_end = max(next_end, max_reach_at[i])
            
            # If we've reached the end of what our current clips cover
            if i == current_end:
                # If the best candidate can't move us forward, we're stuck
                if next_end <= i:
                    # Unless we've already reached the goal
                    if current_end >= time:
                        break
                    return -1
                
                # "Commit" to the candidate that reached next_end
                current_end = next_end
                count += 1
                
                # If we've reached or passed the goal, we're done
                if current_end >= time: 
                    break
                    
        return count
