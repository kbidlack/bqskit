"""This module implements the U1qGate."""
from __future__ import annotations

import math

from openqudit.expressions import UnitaryExpression

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class U1qGate(Gate, CachedClass):
    """
    The Quantinuum U1q single qubit gate.

    It is given by the following parameterized unitary:

    .. math::

        \\begin{pmatrix}
        \\cos{\\frac{\\theta_0}{2}} &
         -i\\exp{-i\\theta_1}\\sin{\\frac{\\theta_0}{2}} \\\\
        -i\\exp{i\\theta_1}\\sin{\\frac{\\theta_0}{2}} &
         \\cos{\\frac{\\theta_0}{2}} \\\\
        \\end{pmatrix}
    """

    _qasm_name = 'U1q'
    _expr = UnitaryExpression(
        'U1q(θ0, θ1) {'
        '['
        '[cos(θ0/2), ~i*e^(~i*θ1)*sin(θ0/2)],'
        '[~i*e^(i*θ1)*sin(θ0/2), cos(θ0/2)]'
        ']'
        '}',
    )


U1qPiGate = U1qGate().with_frozen_params({0: math.pi})
U1qPi2Gate = U1qGate().with_frozen_params({0: math.pi / 2})
