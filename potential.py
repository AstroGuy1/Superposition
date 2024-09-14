# potential.py
import numpy as np

class Potential:
    def __init__(self, expression):
        self.expression = expression  # String expression of the potential

    def construct_potential_operator(self, mesh):
        # Evaluate the potential expression over the mesh grid
        x, y, z = mesh.get_coordinates()
        local_vars = {'x': x, 'y': y, 'z': z, 'np': np}
        V_eval = eval(self.expression, {}, local_vars)
        V_flat = V_eval.ravel()
        return V_flat  # Return as a flat array for operator construction
