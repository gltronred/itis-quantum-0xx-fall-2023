import cirq

class ZX(cirq.Gate):
    def __init__(self):
        super(ZX, self)

    def _num_qubits_(self):
        return 2

    def _decompose_(self, qubits):
        a, b = qubits
        yield cirq.X(a)
        yield cirq.Z(b)

    def _circuit_diagram_info_(self, args):
        return ["X", "Z"]


ZX_gate = ZX()

q1, q2, q3 = cirq.LineQubit.range(3)
c = cirq.Circuit()
c.append(cirq.H(q1))
c.append(cirq.H(q2))
c.append(cirq.X(q3))

c.append(cirq.CNOT(q1, q3))
# c.append(cirq.X(q3).controlled_by(q1))

c.append(ZX_gate(q1, q2).controlled_by(q3))

print(c)

sim = cirq.Simulator()
r = sim.simulate(c)
print(r)
