import numpy as np
import math
import scipy


if __name__ == "__main__":
    n = 1000
    c = 3
    combs = scipy.special.comb(n, c)
    print(f"number of possible clusters of size {c} from a set of {n} points: {combs}")

    
