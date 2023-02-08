from typing import Tuple


class Configuration(object):
    def __init__(self,
                 block_size: int = 32,
                 nn: int = 2,
                 nf: int = 188,
                 nd: int = 50,
                 p: Tuple[
                     float, float, float, float, float, float, float
                 ] = (
                         1.80, 1.80, 1.80, 0.0125, 0.0125, 0.0125, 0.0125
                 ),
                 t1: float = 2.80,
                 t2: float = 0.02
                 ):
        """
        Object to contain the configuration parameter.

        Args:
            block_size (int): The block size of the image pointer (eg. 32, 64, 128).
                The smaller the block size, the more accurate the result is, but takes more time, vice versa.
            nn (int): The amount of neighboring block to be evaluated (Nn)
            nf (int): Minimum threshold of the offset's frequency (Nf)
            nd (int): Minimum threshold of the offset's magnitude (Nd)
            p (int): todo: elaborate this according to the second paper
            t1 (int): todo: elaborate this according to the second paper
            t2 (int): todo: elaborate this according to the second paper

        Returns: None
        """

        self.block_dimension = block_size

        # first algorithm parameter
        self.nn = nn
        self.nf = nf
        self.nd = nd

        # second algorithm parameter
        self.p = p
        self.t1 = t1
        self.t2 = t2
