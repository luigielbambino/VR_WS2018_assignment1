from builtins import range
import math

class TMatrix:
    # width = 4
    # height = 4
    # matrix = [[0 for x in range(width)] for y in range(height)]
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix = [[], [], [], []]

    def __init__(self, passed_in_matrix):
        self.matrix = passed_in_matrix

    def mult(self, other_matrix):
        result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(other_matrix[0])):
                for k in range(len(other_matrix)):
                    result[j][i] += self.matrix[k][i] * other_matrix[j][k]
        for r in result:
            print(r)


def make_trans_mat(x, y, z):
    matrix_trans = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
    trans = TMatrix(matrix_trans)
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


# def make_rot_mat(self, degree, axis):

# def make_scale_mat(self, sx, sy, sz):


class Vector4:
    # Class to store 3D points in homogeneous coordinates
    def __init__(self, x=0, y=0, z=0, w=1):
        self.vector = [x, y, z, w]


def euclidean_distance(p, v):
    # Function to calculate euceldian distance between two given vectors
    for i in range(len(p)):
        p[i] = p[i]/p[len(p)-1]
        v[i] = v[i]/v[len(p)-1]

    distance = ((p[0]-v[0])**2 + (p[1]-v[1])**2 + (p[2]-v[2])**2)**.5
    print("Euclidean distance between: " + str(p) + " and " + str(v) + ": " + str(distance))
    return distance


def main():
    matrix = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
    a = TMatrix(matrix)

    passed_matrix = [[1, 9, 2, 10], [3, 11, 4, 12], [5, 13, 6, 14], [7, 15, 8, 16]]
    TMatrix.mult(a, passed_matrix)

    make_trans_mat(1, 2, 3)

    v1 = Vector4(2, 4, 6, 2)
    v2 = Vector4(0, 0, 0, 1)
    ed = euclidean_distance(v1.vector, v2.vector)


if __name__ == '__main__':
    main()
