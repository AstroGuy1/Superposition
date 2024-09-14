# quantum_solver.py
import numpy as np
from qutip import Qobj, tensor, basis, mesolve
from potential import Potential
from mesh import Mesh
from parallel_compute import parallel_eigensolver

class QuantumSolver:
    def __init__(self, potential, mesh):
        self.potential = potential
        self.mesh = mesh
        self.H = None  # Hamiltonian

    def construct_hamiltonian(self):
        # Construct kinetic and potential energy operators
        T = self.mesh.construct_kinetic_operator()
        V = self.potential.construct_potential_operator(self.mesh)
        self.H = T + V

    def solve_stationary_states(self, num_states=5):
        if self.H is None:
            self.construct_hamiltonian()
        eigenvalues, eigenstates = parallel_eigensolver(self.H, num_states)
        return eigenvalues, eigenstates

    def solve_time_evolution(self, initial_state, tlist):
        if self.H is None:
            self.construct_hamiltonian()
        result = mesolve(self.H, initial_state, tlist, [], [])
        return result
