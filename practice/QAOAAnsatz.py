from qiskit.circuit.library import QAOAAnsatz
from qiskit.quantum_info import SparsePauliOp
ham = SparsePauliOp(["ZZ"]) #2-qubit rule
qaoa = QAOAAnsatz(ham, reps = 1) #1 layer
qaoa.measure_all()
print(qaoa.decompose().draw('text'))