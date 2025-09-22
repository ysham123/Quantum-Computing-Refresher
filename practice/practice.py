from sre_parse import State
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)
print(qc.draw('text'))

from qiskit.quantum_info import Statevector
qc = QuantumCircuit(1)
qc.h(0)

print(Statevector.from_instruction(qc).probabilities())


from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.h(0)

print(Statevector.from_instruction(qc).probabilities())

#quantum gate

from qiskit import QuantumCircuit
qc = QuantumCircuit(2)
qc.x(0)
qc.cx(0,1)
print(Statevector.from_instruction(qc).probabilities())

#superposition and entanglement
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
print(Statevector.from_instruction(qc).probabilities())
print(qc.draw('text'))

from qiskit.circuit.library import TwoLocal
two_local = TwoLocal(3, 'rx', 'cz')
bound = two_local.assign_parameters([0.1] * 12)
print(bound.decompose().draw('text'))

