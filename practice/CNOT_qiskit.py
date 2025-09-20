from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.x(0)
qc.z(1)
qc.cx(0,1)
qc.measure_all()
print(qc.draw())