import pennylane as qml
dev = qml.device('default.qubit', wires = 1)
@qml.qnode(dev)

def qubit_state():
    return qml.state()
print(qubit_state())