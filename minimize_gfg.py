class Solution:
    def minimiseExpression(self, a, n):
        # sum(a) is highly optimized in Python
        total_sum = sum(a)
        
        # Using integer division // because the problem guarantees integer average
        x = total_sum // n
        
        return x

# Example usage
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    # Taking space-separated input and converting to a list of ints
    a = list(map(int, input("Enter elements: ").split()))
    
    sol = Solution()
    print(f"The value of X is: {sol.minimiseExpression(a, n)}")