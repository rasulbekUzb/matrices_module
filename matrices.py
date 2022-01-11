class Matrix:
    def __init__(self, vectors):
        self.m = len(vectors)
        self.n = len(vectors[0])
        self.transformation = vectors

    def __getitem__(self, i):
        try:
            return self.transformation[i]
        except IndexError:
            print("Bunday indeksli element mavjud emas")

    def __call__(self, matrix):
        k = len(matrix.transformation[0])
        transformed_matrix = [[0 for _ in range(k)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(k):
                for p in range(self.n):
                    transformed_matrix[i][j] += self[i][p] * matrix[p][j]
        return Matrix(transformed_matrix)

    def __add__(self, matrix):
        Ctrecker = Matrix(self.transformation.copy())
        for i in range(self.m):
            for j in range(self.n):
                Ctrecker.transformation[i][j] = self[i][j] + matrix[i][j]
        return Ctrecker

    def __sub__(self, matrix):
        Ctrecker = Matrix(self.transformation.copy())
        for i in range(self.m):
            for j in range(self.n):
                Ctrecker.transformation[i][j] = self.transformation[i][j] - matrix.transformation[i][j]
        return Ctrecker

    def transpose(self):
        b = [[0 for _ in range(self.m)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                b[i][j] = self.transformation[j][i]
        return Matrix(b)

    def beauty_print(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self[i][j], end=" ")
            print()
        print()

    def is_square(self):
        return self.m == self.n

def beauty_read():
    array_list = []
    while True:
        l = input()
        if l == '_':
            break
        array_list.append(l.split(' '))
    array_list_inted = array_list.copy()
    for i in range(len(array_list)):
        for j in range(len(array_list[0])):
            array_list_inted[i][j] = int(array_list[i][j])

    return array_list_inted

def beauty_print(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print()
        print()


