from qiskit.circuit.library import TwoLocal

two_local = TwoLocal(3, rotation_blocks = "rx", entanglement_blocks = "cz") # 3 qubits
bound = two_local.assign_parameters([0] * 12) # set all sliders to 0
print(bound.decompose().draw('text'))

#rx rotates each qubit like a spinning coin, and CZ link pairs like gluing coins together.
#Parameters(sliders) let you tune the circuit for optimization