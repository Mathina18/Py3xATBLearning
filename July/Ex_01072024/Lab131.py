# Hierarchical Inheritance

# Father - Multiple Children

class Father():
    def BHK1(self):
        print("1BHK")


class son1(Father):
    def BHK2(self):
        print("2BHK")


class son2(Father):
    def BHK3(self):
        print("3BHK")


class son3(Father):
    def No_House(self):
        print("No House")


son1object = son1()
son1object.BHK2()
son1object.BHK1()

son2object = son2()
son2object.BHK3()
son2object.BHK1()

son3object = son3()
son3object.No_House()
son3object.BHK1()
