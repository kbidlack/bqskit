"""This module implements the U2Gate."""
from __future__ import annotations

from openqudit.expressions import U2Gate as _U2Gate

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class U2Gate(Gate, CachedClass):
    """
    The U2 single qubit gate.

    It is given by the following parameterized unitary:

    .. math::

        \\begin{pmatrix}
        \\frac{\\sqrt{2}}{2} & -\\exp({i\\theta_1})\\frac{\\sqrt{2}}{2} \\\\
        \\exp({i\\theta_0})\\frac{\\sqrt{2}}{2} &
         \\exp({i(\\theta_0 + \\theta_1)})\\frac{\\sqrt{2}}{2} \\\\
        \\end{pmatrix}
    """

    _expr = _U2Gate()
