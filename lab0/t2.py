import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"


if __name__ == "__main__":
    n=int(input())
    matrix=[]
    for i in range(0,n):
        line=input()
        row = [cell if cell == '#' else 0 for cell in line.split()] 
        matrix.append(row)
    rows = n
    cols = n
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '#':
                continue  
            x=0
            for a in range (max(0,i-1),min(rows,i+2)):
                for b in range(max(0, j - 1), min(cols, j + 2)):
                    if matrix[a][b]=='#':
                        x+=1
            matrix[i][j]=x
                
    for i in matrix:
        print('   '.join(map(str, i)))