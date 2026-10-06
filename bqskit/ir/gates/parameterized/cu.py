"""This module implements the CUGate."""
from __future__ import annotations

from openqudit.expressions import Controlled as _Controlled
from openqudit.expressions import U3Gate as _U3Gate

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class CUGate(
    Gate,
    CachedClass,
):
    """
    A gate representing an arbitrary controlled rotation.

    It is given by the following parameterized unitary:

    .. math::

        \\begin{pmatrix}
        1 & 0 & 0 & 0 \\\\
        0 & 1 & 0 & 0 \\\\
        0 & 0 & \\exp{i\\gamma}cos(\\frac{\\theta}{2})
        & -\\exp{i(\\gamma + \\lambda)}sin(\\frac{\\theta}{2}) \\\\
        0 & 0 & \\exp{i(\\gamma + \\phi)}sin(\\frac{\\theta}{2})
        & \\exp{i(\\gamma + \\phi + \\lambda)}cos(\\frac{\\theta}{2}) \\\\
        \\end{pmatrix}
    """

    _qasm_name = 'cu'
    _expr = _Controlled(_U3Gate())
