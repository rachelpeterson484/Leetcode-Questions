class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr_index = m + n - 1
        m_index = m - 1
        n_index = n - 1
            
        # Iterate through array, starting at largest numbers first
        # Track each numbers separately through m_index and n_index
        while (n_index >= 0 and m_index >= 0):
            m_value = nums1[m_index] # 2, 2, index = 0
            n_value = nums2[n_index] # 1, index = 0

            if n_value >= m_value:
                print("setting index: ", arr_index, " to ", nums2[n_index])
                nums1[arr_index] = nums2[n_index]
                n_index = n_index - 1
            else:
                print("setting index: ", arr_index, " to ", nums1[m_index])
                nums1[arr_index] = nums1[m_index]
                m_index = m_index - 1
            arr_index = arr_index - 1
        
        # Edge case 
        while n_index >= 0:
            nums1[arr_index] = nums2[n_index]
            arr_index = arr_index - 1
            n_index = n_index - 1