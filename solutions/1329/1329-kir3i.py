class Solution:
    def diagonalSort(self, mat):
        my = len(mat)
        mx = len(mat[0])

        matD = self.toDiagonal(mat, mx, my)

        for line in matD:
            line.sort()

        return self.toRectagle(matD, mx, my)


    def toDiagonal(self, mat, mx, my):
        rtn = []

        for y_base in range(my-1, 0, -1):
            line = []
            for i in range(mx):
                if i+y_base >= my:
                    break
                line.append(mat[i+y_base][i])
            rtn.append(line)    # make one diagonal line

        for x_base in range(mx):
            line = []
            for i in range(my):
                if i+x_base >= mx:
                    break
                line.append(mat[i][i+x_base])
            rtn.append(line)
        return rtn

    def toRectagle(self, matD, mx, my):
        rtn = [[0]*mx for _ in range(my)]

        for y_base in range(my-1, 0, -1):
            for i in range(mx):
                if i+y_base >= my:
                    break
                rtn[i+y_base][i] = matD[my-1-y_base][i]

        for x_base in range(mx):
            for i in range(my):
                if i+x_base >= mx:
                    break
                rtn[i][i+x_base] = matD[my-1+x_base][i]

        return rtn
