"""This module implements the CRZGate."""
from __future__ import annotations

from openqudit.expressions import Controlled as _Controlled
from openqudit.expressions import RZGate as _RZGate

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class CRZGate(
    Gate,
    CachedClass,
):
    """
    A gate representing a controlled Z rotation.

    It is given by the following parameterized unitary:

    .. math::

        \\begin{pmatrix}
        1 & 0 & 0 & 0 \\\\
        0 & 1 & 0 & 0 \\\\
        0 & 0 & \\exp({-i\\frac{\\theta}{2}}) & 0 \\\\
        0 & 0 & 0 & \\exp({i\\frac{\\theta}{2}}) \\\\
        \\end{pmatrix}
    """

    _expr = _Controlled(_RZGate())
    _qasm_name = 'crz'
