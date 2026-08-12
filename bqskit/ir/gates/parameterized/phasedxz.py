"""This module implements the PhasedXZGate."""
from __future__ import annotations

from openqudit.expressions import UnitaryExpression as _UnitaryExpression

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class PhasedXZGate(Gate, CachedClass):
    """
    A gate representing an Google's PhasedXZGate.

    References:
        https://quantumai.google/reference/python/cirq/PhasedXZGate
    """

    _qasm_name = 'pxz'
    _expr = _UnitaryExpression(
        'PhasedXZ(t0,t1,t2) { '
        '[[e^(i*pi*t0/2)*cos(pi*t0/2),'
        ' e^(i*pi*(t0/2-t2))*(~i*sin(pi*t0/2))],'
        '[e^(i*pi*(t0/2+t1+t2))*(~i*sin(pi*t0/2)),'
        ' e^(i*pi*(t0/2+t1))*cos(pi*t0/2)]] }',
    )
