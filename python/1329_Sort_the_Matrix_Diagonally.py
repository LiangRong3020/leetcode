class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        result_mat= mat[:]
        height= len(mat)
        width=len(mat[0])

        dealed_list= []

        for i in range(height):
            for j in range(width):
                if (i, j) in dealed_list:
                    continue

                tmp_list= [(i, j)]
                tmp_value= [mat[i][j]]
                tmp_i = i +1
                tmp_j= j +1
                while tmp_i < height and tmp_j < width:
                    tmp_list.append((tmp_i, tmp_j))
                    tmp_value.append(mat[tmp_i][tmp_j])

                    tmp_i += 1
                    tmp_j += 1

                tmp_value.sort()

                for element, value in zip(tmp_list, tmp_value):
                    result_mat[element[0]][element[1]]  = value

        return result_mat

