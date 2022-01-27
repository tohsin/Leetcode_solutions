def matrixReshape( mat, r: int, c: int):
        soln=[]
        for i in range(r):
            soln.append([]*c)
        cache=[]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                cache.append(mat[row][col])
        step=0
        for row in range(len(soln)):
            for col in range(len(soln[0])):
                soln[row][col]=cache[step]
                step+=1
        return soln

matrixReshape()