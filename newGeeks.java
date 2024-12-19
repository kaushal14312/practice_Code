class Solution {
    public int kthMissing(int[] arr, int k) {
        int current = 1; // Start checking from the first positive integer
        int missingCount = 0; // Count of missing numbers
        int index = 0; // Index for the input array

        while (missingCount < k) {
            // If the current number is in the array, move to the next number in the array
            if (index < arr.length && arr[index] == current) {
                index++;
            } else {
                // Current number is missing
                missingCount++;
                // If we have found the kth missing number, return it
                if (missingCount == k) {
                    return current;
                }
            }
            // Move to the next positive integer
            current++;
        }

        // In case we exit the loop without returning (should not happen in theory)
        return -1; // This line is just a fallback; ideally, we should always return within the loop.
    }
}