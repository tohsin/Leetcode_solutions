
def numMagicSquaresInside(grid) -> int:
    ans=0
    if (len(grid)<3 )or ( len(grid[0]) <3):
            return 0
        
    for row in range(len(grid)-2):
        for col in range(len(grid[0])-2):
            cache=set()
            diag1=grid[row][col]+grid[row+1][col+1]+grid[row+2][col+2]
            diag2=grid[row][col+2]+grid[row+1][col+1]+grid[row+2][col]
            r1=grid[row][col] +  grid[row][col+1] + grid[row][col+2]
            r2=grid[row+1][col] +  grid[row+1][col+1] + grid[row+1][col+2]
            r3=grid[row+2][col] +  grid[row+2][col+1] + grid[row+2][col+2]
            c1=grid[row][col] + grid[row+1][col] + grid[row+2][col]
            c2=grid[row][col] + grid[row+1][col] + grid[row+2][col]
            c3=grid[row][col] + grid[row+1][col] + grid[row+2][col]
            if diag1==diag2==r1==r2==r3==c1==c2==c3 :
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if grid[i][j]<=9 and grid[i][j]>0: 
                            cache.add(grid[i][j])
                if len(cache)==9:
                    ans+=1
            else:
                continue
    return ans
               




        
print(numMagicSquaresInside([[3,10,2,3,4],[4,5,6,8,1],[8,8,1,6,8],[1,3,5,7,1],[9,4,9,2,9]]))