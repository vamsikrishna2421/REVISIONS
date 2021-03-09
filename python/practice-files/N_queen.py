
global N
N=4

def isSafe(M,row,col):
    for i in range(col):
        if M[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if M[i][j]==1:
            return False
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if M[i][j]==1:
            return False
    return True

def placeq(M,col):
    if col>=N:
        return True
    for i in range(N):
        if isSafe(M,i,col):
            M[i][col]=1
            # print('placing queen at {},{}'.format(i,col))
            if placeq(M,col+1)==True:
                return True
            M[i][col]=0
    return False


if __name__=='__main__':
    M=[[0 for i in range(N)] for j in range(N)]
    if(placeq(M,0)==True):
        print(M)
    else:
        print('solution doesnt exist')
    
    
