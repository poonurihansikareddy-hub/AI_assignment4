districts = ['Adilabad', 'Nizamabad', 'Karimnagar', 'Warangal', 'Khammam']
colors = ['Red', 'Green', 'Blue', 'Yellow']

neighbors = {
    'Adilabad': ['Nizamabad'],
    'Nizamabad': ['Adilabad', 'Karimnagar'],
    'Karimnagar': ['Nizamabad', 'Warangal'],
    'Warangal': ['Karimnagar', 'Khammam'],
    'Khammam': ['Warangal']
}

def is_valid(region, color, assignment):
    for neighbor in neighbors.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    unassigned = [d for d in districts if d not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[unassigned]

    return None

print(backtrack({}))
