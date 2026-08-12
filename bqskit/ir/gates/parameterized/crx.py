"""This module implements the CRXGate."""
from __future__ import annotations

from openqudit.expressions import Controlled as _Controlled
from openqudit.expressions import RXGate as _RXGate

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class CRXGate(
    Gate,
    CachedClass,
):
    """
    A gate representing a controlled X rotation.

    It is given by the following parameterized unitary:

    .. math::

        \\begin{pmatrix}
        1 & 0 & 0 & 0 \\\\
        0 & 1 & 0 & 0 \\\\
        0 & 0 & \\cos{\\frac{\\theta}{2}} & -\\sin{\\frac{\\theta}{2}}i \\\\
        0 & 0 & -\\sin{\\frac{\\theta}{2}}i & \\cos{\\frac{\\theta}{2}} \\\\
        \\end{pmatrix}
    """

    _expr = _Controlled(_RXGate())
