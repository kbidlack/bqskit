"""This module implements the U3Gate."""
from __future__ import annotations

import numpy as np
from openqudit.expressions import U3Gate as _U3Gate

from bqskit.ir.gate import Gate
from bqskit.ir.gates.generalgate import GeneralGate
from bqskit.qis.unitary.unitary import RealVector
from bqskit.qis.unitary.unitarymatrix import UnitaryMatrix
from bqskit.utils.cachedclass import CachedClass


class U3Gate(GeneralGate, CachedClass):
    """
    The U3 single qubit gate.

    It is given by the following parameterized unitary:

    .. math::

        \\begin{pmatrix}
        \\cos{\\frac{\\theta_0}{2}} &
        -\\exp({i\\theta_2})\\sin{\\frac{\\theta_0}{2}} \\\\
        \\exp({i\\theta_1})\\sin{\\frac{\\theta_0}{2}} &
        \\exp({i(\\theta_1 + \\theta_2)})\\cos{\\frac{\\theta_0}{2}} \\\\
        \\end{pmatrix}
    """

    # for some reason openqudit names the U1 gate 'U1'
    # but U3 as U
    _qasm_name = 'u3'
    _expr = _U3Gate()

    def calc_params(self, utry: UnitaryMatrix) -> list[float]:
        """
        Calculate the three parameters to a U3Gate from a given unitary.

        Args:
            utry (UnitaryMatrix): The single-qubit unitary matrix to
                calculate a U3Gate's parameters for.

        Returns:
            list[float]: The three parameters to a U3Gate,
                such that, `U3Gate().get_unitary` will return `utry`.

        Raises:
            ValueError: If `utry` is not a single-qubit unitary.
        """
        if utry.radixes != (2,):
            raise ValueError('Expected single-qubit unitary.')

        mag = np.linalg.det(utry.numpy) ** (-1 / 2)
        special_utry = mag * utry
        a = np.angle(special_utry[1, 1])
        b = np.angle(special_utry[1, 0])
        c = np.abs(special_utry[1, 0])
        d = np.abs(special_utry[0, 0])
        theta = 2 * float(np.arctan2(c, d))
        phi = (a + b)
        lamb = (a - b)
        return [theta, phi, lamb]

    def get_inverse_params(self, params: RealVector = []) -> RealVector:
        """Return the parameters that invert the gate, see :class:`Gate`."""
        self.check_parameters(params)
        return [-params[0], -params[2], -params[1]]

    def get_inverse(self) -> Gate:
        """Return the inverse of this gate."""
        return U3Gate()
