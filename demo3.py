import cirq

# Для отдельных кубитов можно задать имена. Это полезно, если ваш алгоритм
# абстрактный или не оптимизирован под конкретную реализацию квантового
# компьютера (где могут быть ограничения на кубиты, к которым применяются
# операции)

q0 = cirq.NamedQubit('source')
q1 = cirq.NamedQubit('target')

print(q0,q1)

# Можно создать кубиты в цепочке, задав для каждого номер или интервал
q3 = cirq.LineQubit(3)

# здесь создаются кубиты LineQubit(0), LineQubit(1), LineQubit(2)
q0, q1, q2 = cirq.LineQubit.range(3)

# Можно создать кубиты в сетке, по отдельности
q4_5 = cirq.GridQubit(4, 5)

# или все сразу. Код создаёт 16 кубитов от (0,0) до (3,3)
qubits = cirq.GridQubit.square(4)

#############################################################################

import cirq_google
print(cirq_google.Sycamore)

#############################################################################

circuit = cirq.Circuit()
qubits = cirq.LineQubit.range(3)
circuit.append(cirq.H(qubits[0]))
circuit.append(cirq.H(qubits[1]))
circuit.append(cirq.H(qubits[2]))
print(circuit)

#############################################################################

circuit2 = cirq.Circuit()
ops = [cirq.H(q) for q in cirq.LineQubit.range(3)]
circuit2.append(ops)
print(circuit2)

#############################################################################

print(cirq.Circuit(cirq.SWAP(q, q + 1) for q in cirq.LineQubit.range(3)))
