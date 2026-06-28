# https://leetcode.com/problems/grumpy-bookstore-owner/
# 1052. Grumpy Bookstore Owner

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)

        bonus = sum(c for c, g in zip(customers[:minutes], grumpy[:minutes]) if g == 1)
        max_bonus = bonus

        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                bonus += customers[i]
            if grumpy[i - minutes] == 1:
                bonus -= customers[i - minutes]
            max_bonus = max(max_bonus, bonus)

        return base + max_bonus