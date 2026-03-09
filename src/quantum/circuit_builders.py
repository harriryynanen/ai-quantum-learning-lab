from qiskit import QuantumCircuit
import numpy as np


def default_probability_circuit(pd_value: float) -> QuantumCircuit:
    if not 0 <= pd_value <= 1:
        raise ValueError("pd_value must be between 0 and 1")

    theta = 2 * np.arcsin(np.sqrt(pd_value))

    qc = QuantumCircuit(1, 1)
    qc.ry(theta, 0)
    qc.measure(0, 0)
    return qc
