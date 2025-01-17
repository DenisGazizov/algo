from typing import List


def doesValidArrayExist(derived: List[int]) -> bool:
    res = 0
    for i in derived:
        res ^= i
    return res == 0 # The xor-sum of the derived array should be 0 since there is always a duplicate occurrence of each element.
