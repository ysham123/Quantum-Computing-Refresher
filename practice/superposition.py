import pennylane as qml
dev = qml.device("default.qubit", wires = 1)
@qml.qnode(dev)

def superposition():
    qml.Hadamard(wires = 0)
    return qml.probs(wires = 0)
print(superposition())