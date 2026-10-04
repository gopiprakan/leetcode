class Solution:
    def checkValidString(self, s: str) -> bool:
        mask = 1

        for ch in s:
            if ch == "(":
                mask <<= 1
            elif ch == ")":
                mask >>= 1
            else:
                mask = (mask << 1) | mask | (mask >> 1)

        return bool(mask & 1)