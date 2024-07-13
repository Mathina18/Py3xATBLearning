class GF:
    def car(self):
        return "Old car"

class F(GF):
    def car(self):
        return "honda civic"

class S(F):
    def car(self):
        return "Lambo"

son = S()
gf = GF()
f = F()
print(gf.car())
print(f.car())
print(son.car())