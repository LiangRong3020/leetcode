class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result_list = []

        nums2_length = len(nums2)

        for n1 in nums1:
            next_index = nums2.index(n1) + 1

            record_ = True
            while next_index < nums2_length:
                if nums2[next_index] > n1:
                    result_list.append(nums2[next_index])
                    record_ = False
                    break

                next_index += 1

            if record_:
                result_list.append(-1)

        return result_list