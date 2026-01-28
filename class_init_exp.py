class Flower:
    def __init__(self, name):
        self.name = name
    def bloom(self):
        print("Flower is blooming")
    def smell(self):
        print("Flower smells good.")

class Rose(Flower):
    def __init__(self, name, scent):
        super().__init__(name)
        self.scent= scent  
    def smell(self):
        print(f"Rose smells good and having some scent {self.scent}")
        


r = Rose("Red Rose", "flowery")
r.bloom()
r.smell()