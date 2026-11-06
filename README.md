# Rotate-String
Given two strings `s` and `goal`, return `true` *if and only if* `s` *can become* `goal` *after some number of shifts on* `s`.  A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.  * For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.
# LeetCode 796: Rotate String

## Problem Description

Given two strings `s` and `goal`, return `true` *if and only if* `s` *can become* `goal` *after some number of shifts on* `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

* For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

### Examples

**Example 1:**
* **Input:** `s = "abcde"`, `goal = "cdeab"`
* **Output:** `true`
* **Explanation:** Rotating `s` to the left by 2 positions moves `"ab"` to the end, resulting in `"cdeab"`, which matches `goal`.

**Example 2:**
* **Input:** `s = "abcde"`, `goal = "abced"`
* **Output:** `false`
* **Explanation:** No sequence of shifts can change the relative order of the characters to match `"abced"`.

### Constraints
* `1 <= s.length, goal.length <= 100`
* `s` and `goal` consist of lowercase English letters.

---

## Solution Approach: The Concatenation Trick

Instead of manually rotating the string character-by-character inside a loop, we can use an elegant property of rotated strings:

1. **Length Check:** If `s` and `goal` do not have the exact same length, `s` can never be rotated into `goal`. We return `false` immediately.
2. **Concatenation Property:** If we concatenate `s` with itself (`s + s`), the resulting string will contain **all possible cyclic rotations** of `s`.
   * *Example:* If `s = "abcde"`, then `s + s = "abcdeabcde"`.
   * Notice how every single rotation (`"bcdea"`, `"cdeab"`, etc.) exists as a substring inside `"abcdeabcde"`.
3. **Substring Search:** If `goal` is a substring of `s + s`, then it is a valid rotation.

---

## Python 3 Solution

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths are different, goal can never be a rotation of s
        if len(s) != len(goal):
            return False
            
        # Check if goal exists inside the doubled string
        return goal in (s + s)
```

---

## Complexity Analysis

* **Time Complexity:** O(N) where N is the length of string `s`. Creating `s + s` takes linear time, and the substring search algorithm (like Python's internal Timsort/Boyer-Moore-Horspool variant) handles the check efficiently under the hood.
* **Space Complexity:** O(N) to allocate memory for the concatenated string `s + s`.

---

## How to Run Tests

You can test this solution locally by instantiating the class:

```python
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.rotateString("abcde", "cdeab"))  # Expected Output: True
    
    # Test case 2
    print(solution.rotateString("abcde", "abced"))  # Expected Output: False
```
