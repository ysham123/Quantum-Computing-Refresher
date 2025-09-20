from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
state = Statevector.from_instruction(qc)
print(state.probabilities())