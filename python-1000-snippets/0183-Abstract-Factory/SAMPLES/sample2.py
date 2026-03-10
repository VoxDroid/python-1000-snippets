# sample2.py
# furniture abstract factory example

class Chair:
    def sit(self):
        pass

class Sofa:
    def lie_on(self):
        pass

class ModernChair(Chair):
    def sit(self):
        return "Sitting on modern chair"

class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on modern sofa"

class VictorianChair(Chair):
    def sit(self):
        return "Sitting on victorian chair"

class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on victorian sofa"

class FurnitureFactory:
    def create_chair(self):
        pass
    def create_sofa(self):
        pass

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    def create_sofa(self):
        return ModernSofa()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()
    def create_sofa(self):
        return VictorianSofa()

if __name__ == '__main__':
    factory = ModernFurnitureFactory()
    print(factory.create_chair().sit())
    print(factory.create_sofa().lie_on())
    factory = VictorianFurnitureFactory()
    print(factory.create_chair().sit())
    print(factory.create_sofa().lie_on())
