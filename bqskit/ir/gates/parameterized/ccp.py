"""This module implements the CCPGate."""

from __future__ import annotations

from openqudit.expressions import Controlled as _Controlled
from openqudit.expressions import PGate as _PGate

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class CCPGate(
    Gate,
    CachedClass,
):
    """
    A gate representing a controlled controlled phase rotation.

    It is given by the following parameterized unitary:

    .. math::

        \\begin{pmatrix}
        1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\\\
        0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\\\
        0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\\\
        0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\\\
        0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\\\
        0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\\\
        0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\\\
        0 & 0 & 0 & 0 & 0 & 0 & 0 & \\exp({i\\theta}) \\\\
        \\end{pmatrix}
    """

    _qasm_name = 'ccp'
    _expr = _Controlled(_Controlled(_PGate()))
