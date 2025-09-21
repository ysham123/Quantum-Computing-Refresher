from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)
print(qc.draw('text'))

from qiskit.quantum_info import Statevector
qc = QuantumCircuit(1)
qc.h(0)

print(Statevector.from_instruction(qc).probabilities())

