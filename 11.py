class grandparent:
    def a():
        print('grandparent class')

class parent(grandparent):
    def b():
        print('parent class')

class child(parent):
    def c():
        print('child class')

d=child

d.c()                        
d.b()
d.a()