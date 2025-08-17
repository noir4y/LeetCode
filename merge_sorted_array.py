from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 の末尾に空きがあるので、後ろから大きい方を詰めていく
        i = m - 1  # nums1 の有効部分の末尾
        j = n - 1  # nums2 の末尾
        k = m + n - 1  # nums1 の末尾（格納位置）

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # nums2 に残りがあればコピー（nums1側はすでに入っているので不要）
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

