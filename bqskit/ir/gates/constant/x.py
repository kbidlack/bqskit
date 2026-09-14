"""This module implements the XGate."""
from __future__ import annotations

from openqudit.expressions import XGate as _XGate

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class XGate(Gate, CachedClass):
    """
    The one-qudit X gate. This is a Clifford gate.

    By default, the XGate is a qubit Pauli-X (NOT) gate. However, it can be
    generalized to qudits by setting the radix parameter during construction.

    It is represented by the following matrix for qubits:

    .. math::

        \\begin{pmatrix}
        0 & 1 \\\\
        1 & 0 \\\\
        \\end{pmatrix}

    However, generally it is given by the following formula (shift operator):

    .. math::

        X = \\sum_{j} |j+1 \\!\\!\\mod d\\rangle\\langle j|

    where `d` is the number of levels (2 levels is a qubit,
    3 levels is a qutrit, etc.)
    """

    _qasm_name = 'x'

    def __init__(self, radix: int = 2) -> None:
        """
        Construct an XGate.

        Args:
            radix (int): The number of qudit levels (>=2). By default, this
                is 2, which is gives a qubit Hadamard gate.

        Raises:
            ValueError: if radix < 2
        """
        self._radix = radix
        self._expr = _XGate(radix)
