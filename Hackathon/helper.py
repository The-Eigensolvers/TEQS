import numpy as np

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

from itertools import*

import qiskit
from qiskit import *

# Representing Data
from qiskit.providers.aer import QasmSimulator, StatevectorSimulator, UnitarySimulator
from qiskit.tools.visualization import plot_histogram, plot_state_city, plot_bloch_multivector

# Almost Equal
from numpy.testing import assert_almost_equal as aae

### Linear Algebra Tools

# Matrices
H = 1/np.sqrt(2)*np.array([[1, 1], [1, -1]])

# Unitary Matrix
U = lambda theta, phi, lam: np.array([[np.cos(theta/2), -np.exp(1j*lam)*np.sin(theta/2)],
                                       [np.exp(1j*phi)*np.sin(theta/2), np.exp(1j*lam + 1j*phi)*np.cos(theta/2)]])

def simul(circ):

    simulator = Aer.get_backend('qasm_simulator')
    results = execute(circ, simulator, shots = 1).result()
    counts = results.get_counts(circ)
    
    return counts

def dagger(mat):
    # Calculate Hermitian conjugate
    mat_dagger = np.conj(mat.T)

    '''# Assert Hermitian identity
    aae(np.dot(mat_dagger, mat), np.identity(mat.shape[0]))'''

    return mat_dagger

def get(circ, types='unitary', nice=True):
    """
    This function return the statevector or the unitary of the inputted circuit

    Parameters:
    -----------
    circ: QuantumCircuit
        Inputted circuit without measurement gate
    types: str ('unitary')
        Get 'unitary' or 'statevector' option
    nice: bool
        Display the result nicely option or just return unitary/statevector as ndarray

    Returns:
    --------
    out: ndarray
        Outputted unitary of statevector

    """

    if types == 'statevector':
        backend = BasicAer.get_backend('statevector_simulator')
        out = execute(circ, backend).result().get_statevector()
    else:
        backend = BasicAer.get_backend('unitary_simulator')
        out = execute(circ, backend).result().get_unitary()

    if nice:
        display(Matrix(np.round(out, 10)))
    else:
        return out


def sim(circ, visual='hist'):
    """
    Displaying output of quantum circuit

    Parameters:
    -----------
    circ: QuantumCircuit
        QuantumCircuit with or without measurement gates
    visual: str ('hist')
        'hist' (counts on histogram) or 'bloch' (statevectors on Bloch sphere) or None (get counts only)

    Returns:
    --------
    counts: dict
        Counts of each CBS state
    """

    # Simulate circuit and display counts on a histogram
    if visual == 'hist':
        simulator = Aer.get_backend('qasm_simulator')
        results = execute(circ, simulator).result()
        counts = results.get_counts(circ)
        display(plot_histogram(counts))

        return counts

    # Get the statevector and display on a Bloch sphere
    elif visual == 'bloch':
        backend = BasicAer.get_backend('statevector_simulator')
        statevector = execute(circ, backend).result().get_statevector()
        get(circ)
        display(plot_bloch_multivector(statevector))

    # Just get counts
    else:
        simulator = Aer.get_backend('qasm_simulator')
        results = execute(circ, simulator).result()
        counts = results.get_counts(circ)

        return counts
