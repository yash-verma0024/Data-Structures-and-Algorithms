class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge list into a dictionary for O(1) lookups
        lookup = {key: value for key, value in knowledge}
        
        res = []
        key_chars = []
        in_bracket = False
        
        for c in s:
            if c == '(':
                in_bracket = True
            elif c == ')':
                in_bracket = False
                key = "".join(key_chars)
                # Replace with the value if found, otherwise "?"
                res.append(lookup.get(key, "?"))
                key_chars = []  # Reset for the next bracket pair
            else:
                if in_bracket:
                    key_chars.append(c)
                else:
                    res.append(c)
                    
        return "".join(res)
