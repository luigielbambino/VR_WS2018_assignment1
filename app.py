from builtins import range
import math


class TMatrix:
    # width = 4
    # height = 4
    # matrix = [[0 for x in range(width)] for y in range(height)]
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    def __init__(self,
                 p11=0, p21=0, p31=0, p41=0,
                 p12=0, p22=0, p32=0, p42=0,
                 p13=0, p23=0, p33=0, p43=0,
                 p14=0, p24=0, p34=0, p44=0):
        self.matrix = [[p11, p12, p13, p14], [p21, p22, p23, p24], [p31, p32, p33, p34], [p41, p42, p43, p44]]

    def mult(self, other_matrix):
        a = self.matrix
        b = other_matrix
        product_matrix = [[0 for col in range(len(a))] for row in range(len(a[0]))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    product_matrix[i][j] += a[k][i] * b[j][k]
        print("Matrix A: " + str(a) + " * Matrix B: " + str(b) + " =  " + str(product_matrix))

    # working on this feature
    def mult_vec(self, vector):
        result = [0 for col in range(len(vector))]
        for i in range(len(self.matrix)):
            for j in range(len(vector)):
                result[i] += self.matrix[j][i] * vector[j]
        print("A * v:" + str(result))


def make_trans_mat(x, y, z):
    trans = TMatrix(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    for i in range(len(trans.matrix)):
        for j in range(len(trans.matrix[i])):
            if j == 0:
                if i == 3:
                    print(x)
                else:
                    print(trans.matrix[i][j])
            elif j == 1:
                if i == 3:
                    print(y)
                else:
                    print(trans.matrix[i][j])
            elif j == 2:
                if i == 3:
                    print(z)
                else:
                    print(trans.matrix[i][j])
            elif j == 3:
                print(trans.matrix[i][j])


def make_rot_mat(degree, axis):
    rot = TMatrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)

    if axis == "x":
        for i in range(len(rot.matrix)):
            for j in range(len(rot.matrix[i])):
                if i == 0:
                    print(rot.matrix[i][j])
                elif i == 1:
                    if j == 1:
                        print(math.cos(degree))
                    elif j == 2:
                        print(math.sin(degree))
                    else:
                        print(rot.matrix[i][j])
                elif i == 2:
                    if j == 1:
                        print(math.sin(degree))
                    elif j == 2:
                        print(math.cos(degree))
                    else:
                        print(rot.matrix[i][j])
                elif i == 3:
                    print(rot.matrix[i][j])
    elif axis == "y":
        for i in range(len(rot.matrix)):
            for j in range(len(rot.matrix[i])):
                if i == 0:
                    if j == 0:
                        print(math.cos(degree))
                    elif j == 2:
                        print(-math.sin(degree))
                    else:
                        print(rot.matrix[i][j])
                elif i == 1:
                    print(rot.matrix[i][j])
                elif i == 2:
                    if j == 0:
                        print(math.sin(degree))
                    elif j == 2:
                        print(math.cos(degree))
                    else:
                        print(rot.matrix[i][j])
                elif i == 3:
                    print(rot.matrix[i][j])
    elif axis == "z":
        for i in range(len(rot.matrix)):
            for j in range(len(rot.matrix[i])):
                if i == 0:
                    if j == 0:
                        print(math.cos(degree))
                    elif j == 1:
                        print(math.sin(degree))
                    else:
                        print(rot.matrix[i][j])
                elif i == 1:
                    if j == 0:
                        print(-math.sin(degree))
                    elif j == 1:
                        print(math.cos(degree))
                    else:
                        print(rot.matrix[i][j])
                elif i == 2:
                    print(rot.matrix[i][j])
                elif i == 3:
                    print(rot.matrix[i][j])
    else:
        print("Invalid axis was entered. Please enter x,y or z. Case sensitive.")


def make_scale_mat(sx, sy, sz):
    scale = TMatrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)

    for i in range(len(scale.matrix)):
        for j in range(len(scale.matrix[i])):
            if i == 0:
                if j == 0:
                    print(scale.matrix[i][j] * sx)
                else:
                    print(scale.matrix[i][j])
            elif i == 1:
                if j == 1:
                    print(scale.matrix[i][j] * sy)
                else:
                    print(scale.matrix[i][j])
            elif i == 2:
                if j == 2:
                    print(scale.matrix[i][j] * sz)
                else:
                    print(scale.matrix[i][j])
            elif i == 3:
                print(scale.matrix[i][j])


class Vector4:
    # Class to store 3D points in homogeneous coordinates
    def __init__(self, x=0, y=0, z=0, w=1):
        self.vector = [x, y, z, w]
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] / self.vector[len(self.vector) - 1]


def euclidean_distance(p, v):
    # Function to calculate euclidean distance between two given vectors
    distance = ((p[0]-v[0])**2 + (p[1]-v[1])**2 + (p[2]-v[2])**2)**.5
    print("Euclidean distance: " + str(distance))
    return distance


def main():
    # Exercise 1.1
    a = TMatrix(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    b = TMatrix(1, 3, 5, 6, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14, 16)
    a.mult(b.matrix)

    # Exercise 1.2
    make_trans_mat(1, 2, 3)
    print("\nmake_rot_mat called with degree: 45 and axis: x")
    make_rot_mat(45, 'x')
    print("\nmake_rot_mat called with degree: 90 and axis: y")
    make_rot_mat(90, 'y')
    print("\nmake_rot_mat called with degree: 120 and axis: z")
    make_rot_mat(120, 'z')
    print("\nmake_scale_mat called with 1,2,3")
    make_scale_mat(1, 2, 3)

    # Exercise 1.3
    v1 = Vector4(2, 4, 6, 2)
    v2 = Vector4(0, 0, 0, 1)
    print("\n")
    ed = euclidean_distance(v1.vector, v2.vector)

    # Exercise 1.4
    v = Vector4(1, 2, 3, 1)
    a.mult_vec(v.vector)


if __name__ == '__main__':
    main()
