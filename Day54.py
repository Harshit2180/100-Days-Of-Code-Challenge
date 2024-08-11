# Question Link
# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos = 0
        neg = 1

        for i in nums:
            if i > 0:
                res[pos] = i
                pos += 2
            else:
                res[neg] = i
                neg += 2

        return res

"""
I started by creating an empty result list res with the same length as nums. I then initialized two pointers, pos for positive numbers and neg for negative numbers, starting at indices 0 and 1, respectively. I iterated through each number in nums. If the number was positive, I placed it at the current pos index in res and moved the pos pointer two steps ahead. If the number was negative, I placed it at the current neg index in res and moved the neg pointer two steps ahead. Finally, I returned the rearranged list res, which now alternates between positive and negative numbers.
"""