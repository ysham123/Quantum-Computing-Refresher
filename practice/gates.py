import pennylane as qml
dev = qml.device('default.qubit', wires = 1)
@qml.qnode(dev)

def flip_qubit():
    qml.PauliX(wires = 0)
    return qml.expval(qml.PauliZ(0))
print(flip_qubit())