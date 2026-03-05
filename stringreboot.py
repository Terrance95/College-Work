class Solution:
    def min_flips(self, s: str) -> int:
        n = len(s)
        flips_pattern_0 = 0
        
        # Enumerate gives us (index, character)
        for i, char in enumerate(s):
            # Checking against pattern starting with '0': 010101
            if i % 2 == 0:
                if char != '0':
                    flips_pattern_0 += 1
            else:
                if char != '1':
                    flips_pattern_0 += 1
        
        # Pattern starting with '1' will always be n - flips_pattern_0
        flips_pattern_1 = n - flips_pattern_0
        
        return min(flips_pattern_0, flips_pattern_1)

if __name__ == "__main__":
    s = input().strip()
    sol = Solution()
    print(sol.min_flips(s))