#!/usr/bin/env python3

import cirq

def add_oracle(qs, c):
    for i in range(2):
        c.append(cirq.CNOT(qs[i], qs[i+2]))
    c.append(cirq.X(qs[3]))
    c.append(cirq.CNOT(qs[1], qs[2]))

qs = cirq.LineQubit.range(6)
c = cirq.Circuit()
add_oracle(qs[0:4],c)
add_oracle(qs[2:6],c)

print(c)

sim = cirq.Simulator()
r = sim.simulate(c)
print(r)
