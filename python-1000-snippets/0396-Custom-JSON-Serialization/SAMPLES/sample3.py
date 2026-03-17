
# sample3.py
# Serialize a dataclass to JSON.

import dataclasses
import json

@dataclasses.dataclass
class Point:
    x: float
    y: float

def main() -> None:
    p = Point(1.2, 3.4)
    print(json.dumps(dataclasses.asdict(p)))

if __name__ == "__main__":
    main()
