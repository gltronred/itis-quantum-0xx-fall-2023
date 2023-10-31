import cirq

# Создаём кубит с именем q
qubit = cirq.NamedQubit('q')

# Схема применяет гейт Адамара и измеряет результат в m
circuit = cirq.Circuit(cirq.H(qubit), cirq.measure(qubit, key='m'))
print("Circuit:")
print(circuit)

# Эмулируем работу схемы несколько раз
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)

