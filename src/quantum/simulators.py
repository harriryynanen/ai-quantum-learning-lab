from qiskit_aer import AerSimulator
from qiskit import transpile


def run_counts(circuit, shots: int = 2000):
    simulator = AerSimulator()
    compiled = transpile(circuit, simulator)
    result = simulator.run(compiled, shots=shots).result()
    return result.get_counts()
