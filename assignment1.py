import math

class TMatrix:
    #Class for creating Matrix Objects
    def __init__(self,
                 p11=0, p21=0, p31=0, p41=0,
                 p12=0, p22=0, p32=0, p42=0,
                 p13=0, p23=0, p33=0, p43=0,
                 p14=0, p24=0, p34=0, p44=0):
        self.IDMatrix = [[p11, p12, p13, p14], [p21, p22, p23, p24], [p31, p32, p33, p34], [p41, p42, p43, p44]]

    def mult(self, other_matrix):
        ma = self.IDMatrix
        mb = other_matrix
        product_matrix = [[0 for col in range(len(ma))] for row in range(len(ma[0]))]

        for i in range(len(ma)):
            for j in range(len(mb[0])):
                for k in range(len(mb)):
                    product_matrix[i][j] += ma[k][i] * mb[j][k]
        return product_matrix


class Vector4:
    #Class to store 3D points in homogeneous coordinates]
    def __init__(self, x=0, y=0, z=0, w=1):
        self.vector = [x, y, z, w]


def euclidean_distance(p, v):
    #function to calculate euceldian distance between two given vectors
    for i in range(len(len(p))):
        p[i] = p[i]/p[3]
        v[i] = v[i]/v[3]
    distance = ((p[0]-v[0])**2 + (p[1]-v[1])**2 + (p[2]-v[2])**2)**.5
    return distance


def main():
    mat_a = TMatrix(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    mat_b = TMatrix(1, 3, 5, 6, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14, 16)
    v1 = Vector4(2, 4, 6, 2)
    v2 = Vector4(0, 0, 0, 1)
    ed = euclidean_distance(v1.vector, v2.vector)

    print(str(mat_a.IDMatrix) + " * " + str(mat_b.IDMatrix) + " = " + str(mat_a.mult(mat_b.IDMatrix)))
    print(ed)


if __name__ == '__main__':
    main()
