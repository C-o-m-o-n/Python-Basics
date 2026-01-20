def addHello(string: str) -> str:
    return f"Hello {string}" 

names = [
    'Betti',
    'Kyle',
    'Quantum',
    'Damilare',
]

## Pre-mappped names
print(names)

## Mapped names with hello greating
print(list(map(addHello, names)))
print(list(map(lambda s: f"Hello {s} from lambda", names)))
