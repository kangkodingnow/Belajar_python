#diamond problem

class A:

    def show(self):
        print("ini adalah show A")

class B(A):
    def show(self):
        print("ini adalah show B")

class C(A):
    def show(self):
        print("ini adalah show c")

class D(B,C):
    pass

objek = D()
objek.show
#help(objek)