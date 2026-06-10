class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = (total + 1) // 2
        
        # Always run binary search on the smaller array to ensure O(log(min(m, n)))
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A)
        
        while l <= r:
            i = (l + r) // 2      # Partition index for A
            j = half - i          # Partition index for B
            
            # Get the elements around the partition boundaries (handle out-of-bounds with infinity)
            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < len(B) else float('inf')
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements: median is the maximum of the left halves
                if total % 2 != 0:
                    return float(max(Aleft, Bleft))
                # Even total elements: median is the average of the middle two elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            elif Aleft > Bright:
                # A's left element is too big; move partition left
                r = i - 1
            else:
                # B's left element is too big; move partition right
                l = i + 1