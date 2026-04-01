regions = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[unassigned]

    return None

print(backtrack({}))