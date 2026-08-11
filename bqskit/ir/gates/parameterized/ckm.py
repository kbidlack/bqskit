"""This module implments the CKMGate."""
from __future__ import annotations

from openqudit.expressions import UnitaryExpression as _UnitaryExpression

from bqskit.ir.gate import Gate
from bqskit.utils.cachedclass import CachedClass


class CKMGate(Gate, CachedClass):
    """
    The Cabibbo-Kobayashi-Maskawa single qutrit gate.

    References:
        - Particle Data Group review:
          https://pdg.lbl.gov/2023/reviews/rpp2022-rev-ckm-matrix.pdf

        - https://link.springer.com/article/10.1007/JHEP01(2019)106

    Notes:
        - Due to the current experimental searches for the exact values
          of the mixing parameters, and to allow for beyond standard
          model physics, we provide the user with the flexibility of
          setting each parameter.
    """

    _num_qudits = 1
    _radixes = (3,)
    _num_params = 4

    _expr = _UnitaryExpression("""CKM<3>(t13, t12, t23, cp) {
        [
            [cos(t13)*cos(t12),
            cos(t13)*sin(t12),
            sin(t13)*e^(~i*cp)],

            [~cos(t23)*sin(t12) - sin(t23)*sin(t13)*cos(t12)*e^(i*cp),
            cos(t23)*cos(t12) - sin(t23)*sin(t13)*sin(t12)*e^(i*cp),
            sin(t23)*cos(t13)],

            [ sin(t23)*sin(t12) - cos(t23)*sin(t13)*cos(t12)*e^(i*cp),
            ~sin(t23)*cos(t12) - cos(t23)*sin(t13)*sin(t12)*e^(i*cp),
            cos(t23)*cos(t13)],
        ]
    }""")
