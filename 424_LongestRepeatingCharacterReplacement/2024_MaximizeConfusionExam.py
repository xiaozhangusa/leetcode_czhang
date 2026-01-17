# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

 

# Example 1:

# Input: answerKey = "TTFF", k = 2
# Output: 4
# Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
# There are four consecutive 'T's.
# Example 2:

# Input: answerKey = "TFFT", k = 1
# Output: 3
# Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
# Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
# In both cases, there are three consecutive 'F's.
# Example 3:

# Input: answerKey = "TTFTTFTT", k = 1
# Output: 5
# Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
# Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
# In both cases, there are five consecutive 'T's.
 

# Constraints:

# n == answerKey.length
# 1 <= n <= 5 * 104
# answerKey[i] is either 'T' or 'F'
# 1 <= k <= n
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # start, end = 0, 0
        # freq = {'T': 0, 'F': 0}
        # flips, res = 0, 0
        # while end < len(answerKey):
        #     freq[answerKey[end]] += 1
        #     flips = min(freq['T'], freq['F'])
        #     # print("flips: ", flips)
        #     while flips > k and start <= end:
        #         # print("answerKey: ", answerKey)
        #         # print("answerKey[start]: ", start, answerKey[start])
        #         freq[answerKey[start]] -= 1
        #         # if freq[answerKey[start]] == 0:
        #         #     del freq[answerKey[start]]
        #         start += 1
        #         flips = min(freq['T'], freq['F'])
        #     # res = max(res, max(freq.values()))
        #     res = max(res, (end + 1 - start))
        #     # print("res: ", res)
        #     end += 1
        # return res
        end = 0
        freq = {'T': 0, 'F': 0}
        flips, res = 0, 0
        while end < len(answerKey):
            freq[answerKey[end]] += 1
            flips = min(freq['T'], freq['F'])
            if flips <= k:
                res += 1
            else:
                # shrink the window from the left, buy no need to keep shrinking. Invariant: the max window sofar is always valid, so we can just shrink it to the left by 1, no need to
                # find a smaller valid window
                # If we have already found a window of length max_size, then what we need to do next is to search for a larger valid window, for example, a window with length max_size + 1. 
                # Therefore, in the following sliding window process, even if the current window with size max_size is not valid, there is no problem, because we have already found a window of length max_size before, so we may as well continue looking for a larger window.
                # Why: 
                # 1. If we have already found a window of length max_size, then what we need to do next is to search for a larger valid window, for example, a window with length max_size + 1.
                # 2. Keep shrinking the window from the left is not a good idea because it may shrink to a smaller valid window, which is not what we want. 
                freq[answerKey[end - res]] -= 1
            end += 1
        return res
