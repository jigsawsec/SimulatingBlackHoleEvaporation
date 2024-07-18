from qiskit import QuantumCircuit, execute

# Define the number of qubits
num_qubits = 4

# Create a quantum circuit
qc = QuantumCircuit(num_qubits)

# Prepare the initial state (black hole and surroundings)
qc.h(range(num_qubits))

# Apply gates to simulate Hawking radiation
for i in range(num_qubits):
    qc.rx(np.pi / 2, i)  # Rotate the qubit to simulate particle emission
    qc.cx(i, (i + 1) % num_qubits)  # Entangle the qubits to simulate radiation

# Measure the final state
qc.measure_all()

# Execute the circuit
job = execute(qc, backend='ibmq_qasm_simulator')
result = job.result()
print(result.get_counts(qc))
