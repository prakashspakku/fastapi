from functools import lru_cache
from math import sqrt
from statistics import mean, median, stdev
from typing import List, Dict

def compute_stats(values: List[float]) -> Dict[str, float]:
    if len(values) < 2:
        return {"count": float(len(values)), "mean": mean(values) if values else 0.0, "median": median(values) if values else 0.0, "stdev": 0.0}
    return {"count": float(len(values)), "mean": mean(values), "median": median(values), "stdev": stdev(values)}

@lru_cache(maxsize=1024)
def prime_factors(n: int) -> List[int]:
    if n <= 1:
        return []
    factors: List[int] = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    f = 3
    while f <= int(sqrt(n)) + 1:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2
    if n > 1:
        factors.append(n)
    return factors
