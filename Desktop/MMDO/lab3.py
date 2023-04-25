import numpy as np

def simplex(c, A, b, maximize=True, artificial=False):
    """
    Implements the simplex method to solve a linear programming problem
    of the form:
    
        maximize c^Tx if maximize=True, minimize c^Tx otherwise
        subject to Ax <= b, x >= 0
    
    If artificial=True, uses the artificial basis method.
    
    Returns the optimal value and an optimal solution x.
    """
    
    m, n = A.shape
    
    if artificial:
        # Add artificial variables to make all constraints equality constraints
        A = np.hstack([A, np.eye(m)])
        c = np.hstack([c, np.zeros(m)])
        xB = np.arange(n, n + m)
    else:
        xB = np.arange(n)
    
    # Initialize tableau
    tableau = np.zeros((m+1, n+m+1))
    tableau[:-1,:-1] = A
    tableau[:-1,-1] = b
    tableau[-1,:-1] = -c if maximize else c
    tableau[-1,-1] = 0
    
    # Perform simplex iterations until optimal solution found
    while True:
        # Find entering variable
        j = np.argmax(tableau[-1,:-1]) if maximize else np.argmin(tableau[-1,:-1])
        if (maximize and tableau[-1,j] <= 0) or (not maximize and tableau[-1,j] >= 0):
            # All reduced costs are nonpositive or nonnegative, optimal solution found
            break
        
        # Find leaving variable
        x = tableau[:-1,-1] / tableau[:-1,j]
        x[x < 0] = np.inf
        i = np.argmin(x)
        if np.isinf(x[i]):
            # Unbounded problem
            return None, None
        
        # Pivot
        tableau[i,:] /= tableau[i,j]
        for k in range(m+1):
            if k != i:
                tableau[k,:] -= tableau[k,j] * tableau[i,:]
        xB[i] = j
        
    # Extract optimal solution
    x = np.zeros(n)
    x[xB < n] = tableau[xB < n,-1]
    
    return -tableau[-1,-1] if maximize else tableau[-1,-1], x

c = np.array([2, -4])
A = np.array([[8, -5], [1, 3], [2, 7]])
b = np.array([16, 2, 9])
print(simplex(c, A, b, maximize=False, artificial=True))
