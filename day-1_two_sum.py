"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy 

My Strategy (in my own words):
1. Two sum with out ascending order, so you can use a hash map to store the indices of the numbers.
2. Logic: Check if the complement (target - current number) exists in the hash map.
3. If it exists, return the indices of the current number and its complement.
4. If it does not exist, add the current number and its index to the hash map.

Time Complexity:
- Brute Force: O(n^2) - Checking each pair of numbers.
- Optimized: O(n) - Single pass through the list with a hash map.

Space Complexity:
O(n) - Space for the hash map to store indices of numbers.

---

Python Solution:
"""

def twosum(nums, target):
    seen_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen_map:
            return [seen_map[complement], i] #i is the current index and seen_map[complement] is the index of the complement
        seen_map[num] = i
    return []  # Return an empty list if no solution is found


if __name__ == "__main__":
     print(twosum([2,7,11,15], 9))  # Output: [0,1]
