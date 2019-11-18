class Matrix:

    def __init__(self,elements):
        self.elements = elements

    def __str__(self):
        res = ''
        for string in self.elements:
            res = res + f"{str(string)}\n"
        return res

    def __add__(self, other):
        res = []
        for i in range(len(self.elements)):
            s1 = self.elements[i]
            s2 = other.elements[i]
            row = []
            for j in range(len(s1)):
                row.append(s1[j] + s2[j])
            res.append(row)
        return Matrix(res)

m = Matrix([[1,2],[3,4]])
n = Matrix([[-1,-2],[-3,-4]])
a = m + n
print(a)