"""This module implements the ClockGate."""
from __future__ import annotations

from openqudit.expressions import ZGate as _ZGate

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class ClockGate(Gate, CachedClass):
    """
    The one-qudit clock (Z) gate. This is a Weyl-Heisenberg gate.

    The clock gate is given by the following formula:

    .. math::
        Z = \\sum_a \\exp(\\frac{2\\pi ai}{d}) |a\\rangle\\langle a|

    where d is the number of levels (2 levels is a qubit,
    3 levels is a qutrit, etc.)

    References:
        - https://arxiv.org/pdf/2302.07966.pdf
    """

    def __init__(self, radix: int = 3) -> None:
        """
        Construct a ClockGate.

        Args:
            radix (int): The number of qudit levels (>=2). Defaults to
                qutrits.

        Raises:
            ValueError: if radix < 2
        """
        self._expr = _ZGate(radix)
