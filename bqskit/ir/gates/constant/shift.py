"""This module implements the ShiftGate."""
from __future__ import annotations

from openqudit.expressions import XGate as _XGate

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class ShiftGate(Gate, CachedClass):
    """
    The one-qudit shift (X) gate. This is a Weyl-Heisenberg gate.

    This gate shifts the state of a qudit up by one level modulo. For
    example, the shift gate on a qubit is the Pauli-X gate. The shift
    gate on a qutrit is the following matrix:

    .. math::

        \\begin{pmatrix}
        0 & 0 & 1 \\\\
        1 & 0 & 0 \\\\
        0 & 1 & 0 \\\\
        \\end{pmatrix}


    The shift gate is generally given by the following formula:

    .. math::
        \\begin{equation}
            X = \\sum_a |a + 1 mod d ><a|
        \\end{equation}

    where d is the number of levels (2 levels is a qubit,
    3 levels is a qutrit, etc.)

    References:
        - https://arxiv.org/pdf/2302.07966.pdf
    """

    def __init__(self, radix: int = 2) -> None:
        """
        Construct a ShiftGate.

        Args:
            radix (int): The number of qudit levels (>=2). Defaults to
                qutrits.

        Raises:
            ValueError: if radix < 2
        """

        self._expr = _XGate(radix)
