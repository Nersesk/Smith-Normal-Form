from math import inf

def dims(M):

    len_row = len(M)
    len_column = len(M[0])
    return (len_row, len_column)


def MinAij(M, s):
    """
    :param M -matrix:
    :param current row:
    :returns min elements index [i,j]:
    """
    len_row, len_column = dims(M)
    ijmin = [s, s]
    valmin=inf
    for i in (range(s, len_row)):
        for j in (range(s, len_column)):
            if (M[i][j] != 0) and (abs(M[i][j]) <= valmin):
                ijmin = [i, j]
                valmin = abs(M[i][j])
    return ijmin

def display(M):
    """
    tpum e Matric@
    :param M matrix:
    """
    r = ""
    for x in M:
        r += f"{x}\n"
    return r + ""


def is_alone(M, s):
    """
    :param Matrix:
    :param current row(column):
    :return True if all elems in current row despite [s,s]  are 0  else False :
    """
    len_rows, len_columns = dims(M)
    if [M[s][x] for x in range(s + 1, len_columns) if M[s][x] != 0] + [M[y][s] for y in range(s + 1, len_rows) if
                                                                       M[y][s] != 0] == []:
        return True
    else:
        return False


def swap_rows(M, i, j):
    """

    :param M matrix:
    :param Matrici i_rd tox:
    :param Matrici j_rd tox:
    :swaps Matrix row i and j:
    """
    tmp = M[i]
    M[i] = M[j]
    M[j] = tmp

def swap_columns(M, i, j):
    """
    :param M-matrix:
    :param i-column:
    :param j-column:
    :swaps matrix i and j columns:
    """
    num_of_columns = len(M)
    for x in range(num_of_columns):
        tmp = M[x][i]
        M[x][i] = M[x][j]
        M[x][j] = tmp


def add_to_row(M, x, k, s):
    """

    :param M-matrix:
    :param x row :
    :param k digit:
    :param s  row
    :row k elements adds row s elements multiplied k times :
    """
    len_rows, len_column = dims(M)
    for tmpj in range(len_column):
        M[x][tmpj] += k * M[s][tmpj]

def add_to_column(M, x, k, s):
    """
    :param M-matrix:
    :param x-column:
    :param k-digit in which we multiply:
    :param s-column:
    """
    len_rows, len_column = dims(M)
    for tmpj in range(len_rows):
        M[tmpj][x] += k * M[tmpj][s]


def change_sign_row(M, x):
    """

    :param M-matrica:
    :param row x:
    :changes rows sign:
    """
    len_rows, len_column = dims(M)
    for tmpj in range(len_column):
        M[x][tmpj] = -1* M[x][tmpj]

def change_sign_column(M, x):
    """

    :param M matrix :
    :param x column x:
    :changes sign for elements in  column x:
    """
    len_rows, len_column = dims(M)
    for tmpj in range(len_column):
        M[tmpj][x] = - M[tmpj][x]


def gcdExtended(a, b):
    """
    :param a:
    :param b:
    :return (a,b),x and y where ax+by =(a,b):
    """
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def final_view(M):
    """
    :param M matrix:
    """
    len_rows, len_column=dims(M)
    for i in range(0, len_rows - 1):
        for j in range(0, len_rows - 1 - i):
            if M[j+1][j+1]!=0 and M[j][j]!=0:
                if M[j+1][j+1] % M[j][j]!=0:
                    g,x,y=gcdExtended(M[j][j],M[j+1][j+1])
                    add_to_row(M,j,y,j+1)
                    add_to_column(M,j+1,x,j)
                    swap_columns(M,j,j+1)
                    gm=int(M[j][j+1]/M[j][j])
                    add_to_column(M,j+1,-1*gm,j)
                    be=int(M[j+1][j]/M[j][j])
                    add_to_row(M,j+1,-be,j)
                    if M[j+1][j+1]<0:
                        change_sign_column(M,j+1)


def Smith_Normal_Form(M):
    len_rows, len_columns = dims(M)
    print(display(M))
    for s in range(len_rows):
        print(f"Step {s+1}/{len_rows}\n")
        print(display(M))
        while not is_alone(M, s):
            i, j = MinAij(M, s)
            swap_rows(M, s, i)
            swap_columns(M, s, j)
            for x in range(s + 1, len_rows):
                if M[x][s] != 0:
                    k = M[x][s] // M[s][s]
                    add_to_row(M, x, -k, s)
            for x in range(s + 1, len_columns):
                if M[s][x] != 0:
                    k = M[s][x] // M[s][s]
                    add_to_column(M, x, -k, s)
            if is_alone(M, s):
                    if M[s][s] < 0:
                        change_sign_column(M, s)
    if M[len_rows-1][len_columns-1]<0:
        change_sign_row(M,len_rows-1)
    final_view(M)
    print("Matrix Smith Normal form is","",display(M),sep="\n")

