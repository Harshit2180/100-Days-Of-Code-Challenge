# Question Link
# https://leetcode.com/problems/fruit-into-baskets/description/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
    
        left = 0
        MaxFruits = 0
        
        for right in range(len(fruits)):
            if fruits[right] in basket:
                basket[fruits[right]] += 1
            else:
                basket[fruits[right]] = 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            MaxFruits = max(MaxFruits, right - left + 1)
        
        return MaxFruits


"""
I started by initializing a dictionary called basket to keep track of the count of each fruit type in the current window, as well as a left pointer and a variable MaxFruits to store the maximum number of fruits collected. I then used a sliding window approach, where the right pointer iterates over each fruit in the fruits array. For each fruit, I either add it to the basket or update its count if it's already present. If the basket contains more than two types of fruits, I shrink the window by moving the left pointer. For each fruit at the left position, I decrease its count in the basket and remove it if its count reaches zero. After adjusting the window, I update MaxFruits with the maximum size of the current valid window. Finally, I return MaxFruits, which holds the largest number of fruits collected with only two types allowed.
"""