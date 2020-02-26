from sab import cal


class jj(cal):
    n=100
    def __init__(self):
        cal.__init__(self,5,6)
    def hy(self):
        return self.som()+self.n
g=jj()
print(g.hy(),"--->")