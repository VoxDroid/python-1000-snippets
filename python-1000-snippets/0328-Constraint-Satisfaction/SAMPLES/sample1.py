"""Map coloring for Australia using constraint satisfaction."""

from typing import Dict, List


def map_coloring(regions: List[str], neighbors: Dict[str, List[str]], colors: List[str]) -> Dict[str, str]:
    assignment: Dict[str, str] = {}

    def is_valid(region: str, color: str) -> bool:
        for neighbor in neighbors.get(region, []):
            if assignment.get(neighbor) == color:
                return False
        return True

    def backtrack(index: int) -> bool:
        if index == len(regions):
            return True
        region = regions[index]
        for color in colors:
            if is_valid(region, color):
                assignment[region] = color
                if backtrack(index + 1):
                    return True
                assignment.pop(region, None)
        return False

    backtrack(0)
    return assignment


if __name__ == "__main__":
    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    neighbors = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": [],
    }
    colors = ["Red", "Green", "Blue"]

    solution = map_coloring(regions, neighbors, colors)
    print("Map coloring:")
    print(solution)
