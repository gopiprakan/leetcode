class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        cur_set = {""}  
        total_union = set()  
        for ch in expression:
            if ch.isalpha():
                cur_set = {word + ch for word in cur_set}
            elif ch == "{":
                stack.append((total_union, cur_set))
                total_union = set()
                cur_set = {""}
            elif ch == ",":
                total_union |= cur_set
                cur_set = {""}
            elif ch == "}":
                inner_set = total_union | cur_set
                prev_union, prev_cur = stack.pop()
                cur_set = {a + b for a in prev_cur for b in inner_set}
                total_union = prev_union
        return sorted(list(total_union | cur_set))