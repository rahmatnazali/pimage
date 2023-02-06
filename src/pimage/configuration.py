from typing import Tuple


class Configuration:
    def __int__(self,
                block_size: int = 32,
                nn: int = 2,
                nf: int = 188,
                nd: int = 50,
                p: Tuple[int] = (1.80, 1.80, 1.80, 0.0125, 0.0125, 0.0125, 0.0125),
                t1: float = 2.80,
                t2: float = 0.02
                ):

        self.block_dimension = block_size

        # first algorithm parameter
        self.nn = nn  # Nn: amount of neighboring block to be evaluated
        self.nf = nf  # Nf: minimum threshold of the offset's frequency
        self.nd = nd  # Nd: minimum threshold of the offset's magnitude

        # second algorithm parameter
        self.p = p
        self.t1 = t1
        self.t2 = t2
