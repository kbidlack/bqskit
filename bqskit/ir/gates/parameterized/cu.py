"""This module implements the CUGate."""
from __future__ import annotations

from openqudit.expressions import UnitaryExpression as _UnitaryExpression

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

    # cannot use `Controlled(U3Gate())` because of global phase
    _qasm_name = 'cu3'
    _expr = _UnitaryExpression(
        'CU(t0,t1,t2,t3) { [[1,0,0,0],[0,1,0,0],'
        '[0,0,e^(i*t3)*cos(t0/2),~e^(i*(t3+t2))*sin(t0/2)],'
        '[0,0,e^(i*(t3+t1))*sin(t0/2),e^(i*(t3+t1+t2))*cos(t0/2)]] }',
    )
