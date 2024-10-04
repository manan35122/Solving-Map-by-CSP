class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, assignment, variable, value):
        # Check if the value assignment satisfies all constraints
        for neighbor in self.constraints[variable]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment  # All variables assigned

        var = self.select_unassigned_variable(assignment)
        for value in self.domains[var]:
            if self.is_consistent(assignment, var, value):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                assignment.pop(var)  # Undo assignment

        return None  # Failure

    def select_unassigned_variable(self, assignment):
        # Simple unassigned variable selection
        return [var for var in self.variables if var not in assignment][0]

    def print_solution(self, assignment):
        print("Map Coloring Solution:")
        for region, color in assignment.items():
            print(f"{region}: {color}")


# Map Coloring Problem for Australia
variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
domains = {var: ['Red', 'Green', 'Blue'] for var in variables}

# Adjacency constraints (neighboring regions can't share the same color)
constraints = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['NSW', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'T': []  # Tasmania has no neighbors
}

# Instantiate CSP solver
map_csp = CSP(variables, domains, constraints)

# Solve the Map Coloring problem
solution = map_csp.backtrack()

# Print the result
if solution:
    map_csp.print_solution(solution)
else:
    print("No solution found.")
