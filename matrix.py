import math


def print_matrix( matrix ):
    for i in matrix:
        for j in i:
            print (str(j) + " "),
        print

# matrix is a square matrix
def ident( matrix ):
    rows = len(matrix)
    if rows < 1:
        return []
    m = new_matrix(rows, rows)
    for i in range(rows):
        for j in range(rows):
            if i == j:
                m[i][j] = 1
    return m


#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m1rows = len(m1)
    m2rows = len(m2)
    if m1rows < 1 or m2rows < 1:
        return []
    m1cols = len(m1[0])
    m2cols = len(m2[0])
    if m1cols != m2rows:
        print "number of cols in first matrix must match number of rows in second matrix"
        return
    new = new_matrix(m1rows, m2cols)
    for i in range(m1rows):
        for j in range(m2cols):
            #print i,j
            sum = 0
            for k in range(m1cols):
                sum += (m1[i][k] * m2[k][j])
            new[i][j] = sum
    del m2[:]
    for i in range(len(new)):
        m2.append([])
        for j in range(len(new[0])):
            m2[i].append(new[i][j])



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

'''
print_matrix(new_matrix(5, 5))
print_matrix(ident([[1, 2, 2],[2, 3,3],[3,4,4],[4,5,6]]))
m1 = [[1,2,3], [4,5,6]]
m2 = [[7,8], [9,10], [11,12]]
matrix_mult(m1, m2)
print_matrix(m2)
#print_matrix(matrix_mult(m1, m2) )
'''
