class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths are different, goal can never be a rotation of s
        if len(s) != len(goal):
            return False
            
        # Check if goal exists inside the doubled string
        return goal in (s + s)