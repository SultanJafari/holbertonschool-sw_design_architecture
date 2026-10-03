#!/usr/bin/env python3
"""
Decorator pattern implementation - Adding a new wrapper (CaramelDecorator).
"""


class Beverage:
    """Base Beverage class."""

    def cost(self) -> int:
        raise NotImplementedError

    def description(self) -> str:
        raise NotImplementedError


class Coffee(Beverage):
    """Concrete Coffee beverage."""

    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class BeverageDecorator(Beverage):
    """Base decorator class."""

    def __init__(self, beverage: Beverage) -> None:
        self._inner = beverage

    def cost(self) -> int:
        return self._inner.cost()

    def description(self) -> str:
        return self._inner.description()


class MilkDecorator(BeverageDecorator):
    """Decorator that adds milk to a beverage."""

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    """Decorator that adds sugar to a beverage."""

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    """Decorator that adds caramel to a beverage."""

    def cost(self) -> int:
        return self._inner.cost() + 15

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main() -> None:
    beverage1 = MilkDecorator(Coffee())
    print(f"{beverage1.description()} {beverage1.cost()}")

    beverage2 = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{beverage2.description()} {beverage2.cost()}")

    beverage3 = CaramelDecorator(
        MilkDecorator(SugarDecorator(Coffee()))
    )
    print(f"{beverage3.description()} {beverage3.cost()}")


if __name__ == "__main__":
    main()
