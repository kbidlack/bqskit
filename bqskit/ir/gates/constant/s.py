"""This module implements the SGate."""
from __future__ import annotations

from openqudit.expressions import SGate as _SGate

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class SGate(Gate, CachedClass):
    """
    The one-qudit S gate. This is a Clifford gate.

    By default, the SGate is a qubit phase (S) gate. However, it can be
    generalized to qudits by setting the radix parameter during construction.
    It is represented by the following matrix for qubits:

    .. math::

        \\begin{pmatrix}
        1 & 0 \\\\
        0 & i \\\\
        \\end{pmatrix}

    However, generally it is given by the following formula:

    .. math::

        S = \\sum_{j} \\omega_d^{j(j-1)/2} |j\\rangle\\langle j|

    where

    .. math::

        \\omega = \\exp(\\frac{2\\pi i}{d})

    and `d` is the number of levels (2 levels is a qubit,
    3 levels is a qutrit, etc.)
    """

    def __init__(self, radix: int = 2) -> None:
        """
        Construct a SGate.

        Args:
            radix (int): The number of qudit levels (>=2). By default, this
                is 2, which is gives a qubit Hadamard gate.

        Raises:
            ValueError: if radix < 2
        """
        self._radix = radix
        self._expr = _SGate(radix)
        _qasm_name = 's'
