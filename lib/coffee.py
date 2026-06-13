class Coffee:
    """Represents a coffee order with size and price."""

    VALID_SIZES = {"Small", "Medium", "Large"}

    def __init__(self, size: str, price: float):
        self.size = size
        self.price = price

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: str):
        if value not in self.VALID_SIZES:
            print("size must be Small, Medium, or Large")
            return
        self._size = value

    def tip(self) -> None:
        print("This coffee is great, here's a tip!")
        self.price += 1
