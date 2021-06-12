
class Node:

    def __init__(self, value=None, weight: int = 1, lefty=None, righty=None):
        if not isinstance(lefty, Node) and isinstance(righty, Node):
            raise TypeError("lefty i righty muszą być typu Node")
        self.lefty: Node = lefty
        self.righty: Node = righty
        self.weight = weight
        self.value = value

    def __lt__(self, other):
        if not isinstance(other, Node):
            raise TypeError("Błędny typ do porównania")
        if self.weight == other.weight:
            return self.value < other.value
        else:
            return self.weight < other.weight

    def __str__(self):
        return f"Korzeń wartość: {self.value} waga: {self.weight}"

    @classmethod
    def merge(cls, lefty, righty):
        if not isinstance(lefty, Node) and isinstance(righty, Node):
            raise TypeError("lefty i righty muszą być typu Node lub None")
        return cls(value=lefty.value + righty.value, weight=lefty.weight+righty.weight, lefty=lefty, righty=righty)

    def print_tree(self, previous: str = ""):
        if self.lefty is not None:
            self.lefty.print_tree(previous=previous + "0")
        if self.righty is not None:
            self.righty.print_tree(previous=previous + "1")

        if self.righty is None and self.lefty is None:
            print(self.value, previous)

    def encode_tree(self, dictonary: dict, previous: str = ""):
        if self.lefty is not None:
            self.lefty.encode_tree(dictonary=dictonary, previous=previous + "0")
        if self.righty is not None:
            self.righty.encode_tree(dictonary=dictonary, previous=previous + "1")

        if self.righty is None and self.lefty is None:
            dictonary[self.value] = previous
