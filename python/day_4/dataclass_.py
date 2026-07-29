from dataclasses import dataclass, field

@dataclass
class Product:
    name:str
    price: float
    in_stock:bool
    items : list[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = "bhupendra"

p1 = Product("condom", 10, True)
print(p1)
p2 = Product("lub", 100, False)
print(p1 == p2)
