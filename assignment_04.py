from mat import Mat
from vec import Vec
from matutil import *

## 10: (f) Linear-combinations matrix-vector multiply
# You are also allowed to use the matutil module
def lin_comb_mat_vec_mult(M, v):
    '''
    Input:
      -M: a matrix
      -v: a vector
    Output: M*v
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    linear-combination definition of matrix-vector multiplication. 
    Examples:
    >>> M=Mat(({'a','b'},{'A','B'}), {('a','A'):7, ('a','B'):1, ('b','A'):-5, ('b','B'):2})
    >>> v=Vec({'A','B'},{'A':4, 'B':2})
    >>> lin_comb_mat_vec_mult(M,v) == Vec({'a', 'b'},{'a': 30, 'b': -16})
    True
    >>> M1=Mat(({'a','b'},{'A','B'}), {('a','A'):8, ('a','B'):2, ('b','A'):-2, ('b','B'):1})
    >>> v1=Vec({'A','B'},{'A':4,'B':3})
    >>> lin_comb_mat_vec_mult(M1,v1) == Vec({'a', 'b'},{'a': 38, 'b': -5})
    True
    '''
    assert(M.D[1] == v.D)
    vec_return = Vec(M.D[0],{})
    colums = []
    matrix_columns = mat2coldict(M)
    for i in v.D:
      result = v[i]*matrix_columns[i]
      colums.append(result)
    for i in M.D[0]:
      result = 0
      for vector in colums:
         result += vector.f[i]
      vec_return[i] = result
    return vec_return      
                



## 11: (Problem 4.17.14) Linear-combinations vector-matrix multiply
def lin_comb_vec_mat_mult(v, M):
    '''
    Input:
      -v: a vector
      -M: a matrix
    Output: v*M
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    linear-combination definition of vector-matrix multiplication. 
    Examples:
      >>> M=Mat(({'a','b'},{'A','B'}), {('a','A'):7, ('a','B'):1, ('b','A'):-5, ('b','B'):2})
      >>> v=Vec({'a','b'},{'a':2, 'b':-1})
      >>> lin_comb_vec_mat_mult(v,M) == Vec({'A', 'B'},{'A': 19, 'B': 0})
      True
      >>> M1=Mat(({'a','b'},{'A','B'}), {('a','A'):8, ('a','B'):2, ('b','A'):-2, ('b','B'):1})
      >>> v1=Vec({'a','b'},{'a':4,'b':3})
      >>> lin_comb_vec_mat_mult(v1,M1) == Vec({'A', 'B'},{'A': 26, 'B': 11})
      True
    '''
    assert(v.D == M.D[0])
    return_vec = Vec(M.D[1], {})
    matrix_columns = mat2rowdict(M)
    columns = []
    for i in v.D:
      result = v[i]*matrix_columns[i]
      columns.append(result)
    for i in M.D[1]:
      result = 0
      for vector in columns:
         result += vector.f[i]
      return_vec[i] = result
    return return_vec     
          
          

            

## 12: (Problem 4.17.15) dot-product matrix-vector multiply
# You are also allowed to use the matutil module
def dot_product_mat_vec_mult(M, v):
    '''
    Return the matrix-vector product M*v.
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    dot-product definition of matrix-vector multiplication. 
    Examples:
    >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
    >>> v=Vec({0,1},{0:4, 1:2})
    >>> dot_product_mat_vec_mult(M,v) == Vec({'a', 'b'},{'a': 30, 'b': -16})
    True
    >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
    >>> v1=Vec({0,1},{0:4,1:3})
    >>> dot_product_mat_vec_mult(M1,v1) == Vec({'a', 'b'},{'a': 38, 'b': -5})
    True
    '''
    assert(M.D[1] == v.D)
    matrix_rows = mat2rowdict(M)
    return_vec = Vec(M.D[0], {})
    for i in M.D[0]:
      return_vec[i] += matrix_rows[i]*v
    return return_vec
      



## 13: (Problem 4.17.16) Dot-product vector-matrix multiply
# You are also allowed to use the matutil module
def dot_product_vec_mat_mult(v, M):
    '''
    The following doctests are not comprehensive; they don't test the
    main question, which is whether the procedure uses the appropriate
    dot-product definition of vector-matrix multiplication. 
    Examples:
      >>> M=Mat(({'a','b'},{0,1}), {('a',0):7, ('a',1):1, ('b',0):-5, ('b',1):2})
      >>> v=Vec({'a','b'},{'a':2, 'b':-1})
      >>> dot_product_vec_mat_mult(v,M) == Vec({0, 1},{0: 19, 1: 0})
      True
      >>> M1=Mat(({'a','b'},{0,1}), {('a',0):8, ('a',1):2, ('b',0):-2, ('b',1):1})
      >>> v1=Vec({'a','b'},{'a':4,'b':3})
      >>> dot_product_vec_mat_mult(v1,M1) == Vec({0, 1},{0: 26, 1: 11})
      True
      '''
    assert(v.D == M.D[0])
    return_vec = Vec(M.D[1], {})
    matrix_rows = mat2coldict(M)
    for label in M.D[1]:
       return_vec[label] += matrix_rows[label]*v
    return return_vec
       


if __name__ == "__main__":
  import doctest
  doctest.testmod()
  # You can add code to test below this line
