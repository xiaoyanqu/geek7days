class Solution:
    def __reverse(self, A, lo, hi):
        if not A or len(A) < 2 or lo >= hi:
            return
        
        while lo < hi:
            A[lo], A[hi] = A[hi], A[lo]
            lo += 1
            hi -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return
        
        k = k % len(nums)
        
        if k == 0:
            return
        
        pivot = len(nums) - k - 1
        
        self.__reverse(nums, 0, pivot)
        self.__reverse(nums, pivot+1, len(nums) - 1)
        self.__reverse(nums, 0, len(nums) - 1)
