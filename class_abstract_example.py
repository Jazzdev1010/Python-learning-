from abc import ABC, abstractmethod


class Flower(ABC):
    # def __init__(self, name):
    #     self.name = name
    @abstractmethod
    def bloom(self):
        pass
    @abstractmethod
    def smell(self):
        pass


class Rose(Flower):
    def __init__(self, name, scent):
        self.name = name
        self.scent= scent  
    def bloom(self):
        print(f"{self.name} is blooming.")
        
    def smell(self):
        print(f"Rose smells good and having some scent {self.scent}")
        

# f = Flower()
r = Rose("Red Rose", "flowery")
r.bloom()
r.smell()