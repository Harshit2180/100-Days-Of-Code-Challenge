# Question Link
# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

        

"""
I started by initializing an empty list res to store valid combinations that sum to the target. Then, I defined a helper function dfs with three parameters: i for the current index in the candidates list, cur for the current combination, and total to track the sum. In the dfs function, if total equals the target, I added a copy of cur to res. If total exceeds the target or the index i goes out of bounds, I returned to stop further exploration. At each step, I explored two options: including the current candidate and calling dfs recursively with the same index, or excluding it and moving to the next index. After recursion, I removed the last element from cur to backtrack. Finally, I called dfs starting at index 0 with an empty combination and returned res with all valid combinations.
"""