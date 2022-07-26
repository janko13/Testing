
from typing import List

def total(xs: List[float]) -> float:
    # return the sum of xs
    result: float = 0.0

    for x in xs:
        result += x

    return result

def join(xs: List[int], delimiter: str) -> str:
    result: str = ""
    for x in xs:
        if result == "":
            result = str(x)
        else:
            result += delimiter + str(x)

    return result