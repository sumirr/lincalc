from sympy import Matrix

A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rref, row_ops = A.rref(simplify=True, pivots=True, normalize_last=True, row_echelon_form=True, reduce_annihilators=False, chop=True, clear=True, tol=None, simplify=_simplify, rankcheck=True, check_rank=True, iszerofunc=None, simplify_x=True, rankcheck_tols=None, inverse=False, zero_division=None, hermite=False, method='gauss')

for op in row_ops:
    print(op)
    
print(rref)

