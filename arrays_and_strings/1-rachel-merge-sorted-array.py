from typing import List 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        arr_index = m + n - 1
        m_index = m - 1
        n_index = n - 1

        # Edge case, where we have m, n = 0, 1. Merge nums2 into nums1
        if m_index < 0:
            nums1[0] = nums2[0]
            
        # Iterate through array, starting at largest numbers first
        # Track each numbers separately through m_index and n_index
        # If nums2 > nums1, set nums2[index] to nums2. Else sest nums2. Decrease indexes
        while (n_index >= 0 and m_index >= 0):
            m_value = nums1[m_index]
            n_value = nums2[n_index]

            if n_value > m_value:
                nums1[arr_index] = nums2[n_index]
                n_index = n_index - 1
            else:
                nums1[arr_index] = nums1[m_index]
                m_index = m_index - 1
                
            arr_index = arr_index - 1
