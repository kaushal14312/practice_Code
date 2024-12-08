from bisect import bisect_right

class Solution:
    # Method to find surpasser count
    def findSurpasser(self, arr):
        n = len(arr)
        result = [0] * n  # Initialize the result list with zeros
        sorted_list = []   # This will hold the sorted elements we have seen so far

        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            current = arr[i]
            # Find the position to insert the current element
            pos = bisect_right(sorted_list, current)
            # The number of surpassers is the number of elements to the right of the position
            result[i] = len(sorted_list) - pos
            # Insert the current element in the sorted list
            sorted_list.insert(pos, current)

        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    arr1 = [4, 5, 1, 2, 3]
    result1 = solution.findSurpasser(arr1)
    print(result1)  # Output: [1, 0, 2, 1, 0]

    arr2 = [2, 7, 5, 3, 8, 1]
    result2 = solution.findSurpasser(arr2)
    print(result2)  # Output: [4, 1, 1, 1, 0, 0]