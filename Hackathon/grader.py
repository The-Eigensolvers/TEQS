from frozen_yoghourt import *


### 1a
def grader1a(A, B, C, T, V, W):
    
    try:
        aae(A@B@C, H@T@V@W@H)
    except:
        return 'T, V, W are not correct'
    else:
        if np.all(V == W):
            return 'Unitary matrices are not unique'
        elif np.all(V == T):
            return 'Unitary matrices are not unique'
        else:
            return 'Congratulations, your answer is correct \U0001F389'

### 1b
def grader1b(A, B, C, D, E, F, H, I, J, K, L, M):
    
    V = np.array([[0, -np.sqrt(2)/2 - np.sqrt(2)/2 * 1j], [1j, 0]])
    
    try:
        aae(A@B@C@D@E@F, V@H@I@J@K@L@M@dagger(V))
    except:
        return 'H, I, J, K, L, M are not correct'
    else:
        return 'Congratulations, your answer is correct \U0001F389'

### 2
def grader2(circ):
    
    correct_mat = np.array([[0, 0, 0, 0, 1/np.sqrt(2), 1/np.sqrt(2), 0, 0],
          [0, 0, 1/np.sqrt(2), -1/np.sqrt(2), 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1/np.sqrt(2), 1/np.sqrt(2)],
          [1/np.sqrt(2), -1/np.sqrt(2), 0, 0, 0, 0, 0, 0],
          [1/np.sqrt(2), 1/np.sqrt(2), 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1/np.sqrt(2), -1/np.sqrt(2)],
          [0, 0, 1/np.sqrt(2), 1/np.sqrt(2), 0, 0, 0, 0],
          [0, 0, 0, 0, 1/np.sqrt(2), -1/np.sqrt(2), 0, 0]])
    
    circ_mat = get(circ, nice = False)
    
    try:
        aae(correct_mat, circ_mat)
    except:
        return 'Circuit is not correct'
    else:
        circ = transpile(circ, basis_gates = ['u', 'cx'])
        no_u = circ.count_ops()['u']
        no_cx = circ.count_ops()['cx']

        cost = 10*no_cx + no_u
        
        print(f"Congratulations \U0001F389! Your answer is correct.  \n\nYour cost is {cost}.\n\nFeel free to submit your answer")
        
def grader3(circ):
    
    correct_mat = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    circ_mat = get(circ, nice = False)
    
    try:
        aae(correct_mat, np.abs(circ_mat))
    except:
        return 'Circuit is not correct'
    else:
        circ = transpile(circ, basis_gates = ['u', 'cx'])
        no_u = circ.count_ops()['u']
        no_cx = circ.count_ops()['cx']
        no_q = circ.num_qubits

        cost = 20*(no_q - 5) + 10*no_cx + no_u
        
        print(f"Congratulations \U0001F389! Your answer is correct.  \n\nYour cost is {cost}.\n\nFeel free to submit your answer")
        
def grader4a(circ):
    correct_mat =  np.array([[0., 0., 0., 0., 1., 0., 0., 0.],
                             [0., 0., 0., 1., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 0., 1., 0.],
                             [0., 1., 0., 0., 0., 0., 0., 0.],
                             [1., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 0., 0., 1.],
                             [0., 0., 1., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 1., 0., 0.]])
    
    circ_mat = get(circ, nice = False)
    
    try:
        aae(correct_mat, np.abs(circ_mat))
    except:
        return 'Circuit is not correct'
    else:
        try:
            no_ccx = circ.count_ops()['ccx']
        except:
            no_ccx = 0
        no_cx = circ.count_ops()['cx']
        circ = transpile(circ, basis_gates = ['u', 'cx'])
        no_u = circ.count_ops()['u']

        cost = 60*no_ccx + 10*no_cx + no_u
        
        print(f"Congratulations \U0001F389! Your answer is correct.  \n\nYour cost is {cost}.\n\nFeel free to submit your answer")
        
def grader4b(circ):
    correct_mat =  np.array([[0., 0., 0., 0., 0., 0., 0., 1.],
                             [0., 1., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 1., 0., 0.],
                             [0., 0., 0., 1., 0., 0., 0., 0.],
                             [1., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 0., 1., 0.],
                             [0., 0., 1., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 1., 0., 0., 0.]])
    
    circ_mat = get(circ, nice = False)
    
    try:
        aae(correct_mat, np.abs(circ_mat))
    except:
        return 'Circuit is not correct'
    else:
        try:
            no_ccx = circ.count_ops()['ccx']
        except:
            no_ccx = 0
        no_cx = circ.count_ops()['cx']
        circ = transpile(circ, basis_gates = ['u', 'cx'])
        no_u = circ.count_ops()['u']

        cost = 60*no_ccx + 10*no_cx + no_u
        
        print(f"Congratulations \U0001F389! Your answer is correct.  \n\nYour cost is {cost}.\n\nFeel free to submit your answer")
        
def grader4c(circ):
    correct_mat =  np.array([[0., 0., 0., 0., 0., 0., 1., 0.],
                             [1., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 1., 0., 0., 0.],
                             [0., 0., 0., 1., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0., 0., 0.],
                             [0., 1., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 1., 0., 0.],
                             [0., 0., 0., 0., 0., 0., 0., 1.]])
    
    circ_mat = get(circ, nice = False)
    
    try:
        aae(correct_mat, np.abs(circ_mat))
    except:
        return 'Circuit is not correct'
    else:
        try:
            no_ccx = circ.count_ops()['ccx']
        except:
            no_ccx = 0
        no_cx = circ.count_ops()['cx']
        circ = transpile(circ, basis_gates = ['u', 'cx'])
        no_u = circ.count_ops()['u']

        cost = 60*no_ccx + 10*no_cx + no_u
        
        print(f"Congratulations \U0001F389! Your answer is correct.  \n\nYour cost is {cost}.\n\nFeel free to submit your answer")