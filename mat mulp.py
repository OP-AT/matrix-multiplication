def mat_ent():
    global nr1, nc1, nr2, nc2
    nr1 = int(input("enter number of rows in first matrix:         "))
    nc1 = int(input("enter number of columns in first matrix:      "))
    nr2 = int(input("enter number of rows in the second matrix:    "))
    nc2 = int(input("enter number of columns of the second matrix: "))
    if nc1 != nr2:
        print("invalid combination!, no. of rows of first matrix should be equal to no. of columns in second matrix")
        mat_ent()


mat_ent()
print(" order of first matrix is: ", nr1, "X", nc1)
print("order of second matrix is: ", nr2, "X", nc2)
#takking inpur for first matrix
mat_A = []
for i in range(1, nr1+1):
    r1v = []
    print("enter elements of row", i,  "of 1st matrix: ")
    for j in range(1, nc1+1):
        r1d = int(input())
        r1v.append(r1d)
    mat_A.append(r1v)
    print(r1v)
print("please check the matrix A entered by you: ")
for rows in mat_A:
    print(rows)
#taking input for  second matrix
mat_B = []
for i in range(1, nc2+1):
    c1v = []
    print("enter elements of column", i, "of second matrix")
    for j in range(1, nr2+1):
        c1d = int(input())
        c1v.append(c1d)
    mat_B.append(c1v)

print("please check matrix b entered by you: ")
for cols in mat_B:
    print(cols)              
# process of multiplication
res_mat = []
for r_row in mat_A:
    res_r = []
    for c_col in mat_B:
        res_d = 0
        for j in range(nc1):
            res_d += r_row[j] * c_col[j]
        res_r.append(res_d)
    res_mat.append(res_r)

print("the resultant matrix is: ")
for rows in res_mat:
    print(rows)
