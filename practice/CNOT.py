import pennylane as qml
dev = qml.device('default.qubit', wires=2)
@qml.qnode(dev)
def gate_circuit():
    qml.PauliX(wires=0)  # |00⟩ → |10⟩
    qml.PauliZ(wires=1)  # No effect on |0⟩
    qml.CNOT(wires=[0,1])  # |10⟩ → |11⟩
    return qml.probs(wires=[0,1])  # Expect [0, 0, 0, 1] (|11⟩)
print(gate_circuit())