"""This module implements the FSIMGate."""
from __future__ import annotations

from openqudit.expressions import UnitaryExpression as _UnitaryExpression

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class FSIMGate(
    Gate,
    CachedClass,
):
    """
    Google's FSIM Gate.

    Contains all two qubit interactions that preserve excitations,
    up to single-qubit rotations and global phase.

    It is given by the following parameterized unitary:

    .. math::
        \\begin{pmatrix}
        1 & 0 & 0 & 0 \\\\
        0 & \\cos{\\theta} & -i\\sin{\\theta} & 0 \\\\
        0 & -i\\sin{\\theta} & \\cos{\\theta} & 0 \\\\
        0 & 0 & 0 & e^{-i\\phi} \\\\
        \\end{pmatrix}

    References:
        https://quantumai.google/reference/python/cirq/ops/FSimGate
    """

    _qasm_name = 'fsim'
    _expr = _UnitaryExpression(
        'FSIM(t0,t1) { [[1,0,0,0],'
        '[0,cos(t0),~i*sin(t0),0],'
        '[0,~i*sin(t0),cos(t0),0],'
        '[0,0,0,e^(~i*t1)]] }',
    )
