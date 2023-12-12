#!/usr/bin/env python3

import cirq
import numpy as np


def make_phase_estimation(n, U, u_bit):
    """Circuit to estimate phase"""
    qubits = cirq.LineQubit.range(n)
    phase_estimator = cirq.Circuit(cirq.H.on_each(*qubits))
    for i, bit in enumerate(qubits):
        phase_estimator.append(cirq.ControlledGate(U).on(bit, u_bit) ** (2**(n - i - 1)))
    phase_estimator.append(cirq.qft(*qubits[::-1], without_reverse=True, inverse=True))
    phase_estimator.append(cirq.measure(*qubits, key='theta'))
    return phase_estimator


# Experiment for X and n=3
n1 = 3
u1 = cirq.NamedQubit('u')
pe1 = make_phase_estimation(n1, cirq.T, u1)
pe1.insert(0, cirq.X(u1))
print(pe1)

sim = cirq.Simulator()
res1 = sim.run(pe1, repetitions = 10)
print(res1.measurements['theta'])
theta1 = np.sum(2 ** np.arange(n1) * res1.measurements['theta'], axis=1) / 2**n1
print(theta1)


# Experiment for 1/3 and theta estimates for 3 bits
n2 = 3
u2 = cirq.NamedQubit('u')
pe2 = make_phase_estimation(n2, cirq.Z**(1/3), u2)
pe2.insert(0, cirq.X(u2))
print(pe2)

res2 = sim.run(pe2, repetitions = 10)
print(res2.measurements['theta'])
theta2 = np.sum(2 ** np.arange(n2) * res2.measurements['theta'], axis=1) / 2**n2
print(theta2)
print(res2.histogram(key = 'theta'))


# 4 bits
n3 = 4
u3 = cirq.NamedQubit('u')
pe3 = make_phase_estimation(n3, cirq.Z**(1/3), u3)
pe3.insert(0, cirq.X(u3))
print(pe3)

res3 = sim.run(pe3, repetitions = 1000)
print(res3.histogram(key = 'theta'))


# 5 bits
n4 = 5
u4 = cirq.NamedQubit('u')
pe4 = make_phase_estimation(n4, cirq.Z**(1/3), u4)
pe4.insert(0, cirq.X(u4))
print(pe4)

res4 = sim.run(pe4, repetitions = 1000)
print(res4.histogram(key = 'theta'))
