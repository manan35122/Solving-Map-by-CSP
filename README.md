# Map Coloring Problem Solver for Australia Using Constraint Satisfaction (CSP)

This project implements a Constraint Satisfaction Problem (CSP) solution for the Map Coloring Problem, specifically for the regions of Australia. The goal is to assign one of three colors (Red, Green, or Blue) to each region such that no two adjacent regions share the same color.

## Regions of Australia

The regions to be colored are:
1. **WA**: Western Australia
2. **NT**: Northern Territory
3. **Q**: Queensland
4. **NSW**: New South Wales
5. **V**: Victoria
6. **SA**: South Australia
7. **T**: Tasmania

## Adjacency Constraints

The following regions are adjacent, meaning they cannot be assigned the same color:
- WA is adjacent to NT and SA.
- NT is adjacent to WA, SA, and Q.
- Q is adjacent to NT, SA, and NSW.
- NSW is adjacent to Q, SA, and V.
- V is adjacent to NSW and SA.
- SA is adjacent to WA, NT, Q, NSW, and V.
- T (Tasmania) has no neighboring regions and can be any color.

## Implementation

### Classes and Functions

- **CSP**: This class encapsulates the CSP solver with the following methods:
  - `__init__(self, variables, domains, constraints)`: Initializes the CSP with given variables, domains, and constraints.
  - `is_consistent(self, assignment, variable, value)`: Checks if assigning a value to a variable is consistent with current assignments.
  - `backtrack(self, assignment={})`: Recursively attempts to assign colors to all regions using backtracking.
  - `select_unassigned_variable(self, assignment)`: Selects the next variable to assign based on a simple strategy.
  - `print_solution(self, assignment)`: Prints the assigned colors for each region.

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/map-coloring-australia.git
2. Navigate to the project directory:
    cd map-coloring-australia
3. Run the Python script:
   python map_coloring.py
# Output
The program will output the solution for the map coloring problem, showing which color is assigned to each region. If no solution is found, it will indicate that as well.
# Example Output
Map Coloring Solution:
WA: Red
NT: Green
Q: Blue
NSW: Red
V: Green
SA: Blue
T: Red
# Contributing
Contributions are welcome! Feel free to open issues, submit pull requests, or suggest improvements.
# License
This project is licensed under the MIT License. See the LICENSE file for details.

### How to Use This README

1. Replace `yourusername` in the cloning URL with your actual GitHub username.
2. Save this content in a file named `README.md` in your project directory.
3. Customize any sections further as needed to better fit your project or style.

Feel free to ask if you need more modifications or additional sections!


