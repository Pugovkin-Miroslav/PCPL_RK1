from dataclasses import dataclass


@dataclass
class House:
    id: int
    number: str
    floors: int
    street_id: int


@dataclass
class Street:
    id: int
    name: str


@dataclass
class HouseStreet:
    house_id: int
    street_id: int


streets = [
    Street(1, "Арбат"),
    Street(2, "Академическая"),
    Street(3, "Тверская"),
]

houses = [
    House(1, "10", 5, 1),
    House(2, "12", 9, 1),
    House(3, "7", 3, 2),
    House(4, "20", 16, 3),
]

house_streets = [
    HouseStreet(1, 1),
    HouseStreet(2, 1),
    HouseStreet(2, 2),
    HouseStreet(3, 2),
    HouseStreet(4, 3),
]


def main():
    streets_with_houses = {
        street.name: [house.number for house in houses if house.street_id == street.id]
        for street in streets
        if street.name.startswith("А")
    }

    max_floors = []
    for street in streets:
        floors = [house.floors for house in houses if house.street_id == street.id]
        if floors:
            max_floors.append((street.name, max(floors)))
    max_floors.sort(key=lambda item: item[1])

    related_houses = sorted(
        [
            (house.number, street.name)
            for link in house_streets
            for house in houses
            for street in streets
            if house.id == link.house_id and street.id == link.street_id
        ],
        key=lambda item: item[1],
    )

    print("Задание Г1. Улицы на букву А и номера домов")
    for street_name, numbers in streets_with_houses.items():
        print(f"{street_name}: {', '.join(numbers)}")

    print("\nЗадание Г2. Улицы по возрастанию максимальной этажности")
    for street_name, floors in max_floors:
        print(f"{street_name}: {floors}")

    print("\nЗадание Г3. Дома и улицы, связь многие-ко-многим")
    for number, street_name in related_houses:
        print(f"Дом {number} — {street_name}")


if __name__ == "__main__":
    main()
