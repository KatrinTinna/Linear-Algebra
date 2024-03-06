## 1: (Problem 1.7.1) Python Comprehensions: Filtering
def my_filter(L, num):
    """
    Input:
      -L: a list of numbers
      -num: a positive integer
    Output:
      -a list of numbers not containing a multiple of num
    Examples:
      >>> my_filter([1,2,4,5,7],2)
      [1, 5, 7]
      >>> my_filter([10,15,20,25],10)
      [15, 25]
    """
    pass


x = my_filter([10, 15, 20, 25], 10)
print(x)

## 2: (Problem 1.7.2) Python Comprehensions: Lists of Lists


def my_lists(L):
    """
    >>> my_lists([1,2,4])
    [[1], [1, 2], [1, 2, 3, 4]]
    >>> my_lists([0,3])
    [[], [1, 2, 3]]
    """
    result = []
    for num in L:
        if num == 0:
            result.append([])
        else:
            current = []
            for number in range(1, num + 1):
                current.append(number)
            result.append(current)
    return result


## 3: (Problem 1.7.3) Python Comprehensions: Function Composition
def my_function_composition(f, g):
    """
    Input:
      -f: a function represented as a dictionary such that g of f exists
      -g: a function represented as a dictionary such that g of f exists
    Output:
      -a dictionary that represents a function g of f
    Examples:
      >>> f = {0:'a',1:'b'}
      >>> g = {'a':'apple','b':'banana'}
      >>> my_function_composition(f,g) == {0:'apple',1:'banana'}
      True

      >>> a = {'x':24,'y':25}
      >>> b = {24:'twentyfour',25:'twentyfive'}
      >>> my_function_composition(a,b) == {'x':'twentyfour','y':'twentyfive'}
      True
    """
    result = {}
    for key, value in f.items():
        result[key] = g[value]
    return result


## 4: (Problem 1.7.4) Summing numbers in a list
def my_sum(L):
    """
        Input:
          a list L of numbers
        Output:
          sum of the numbers in L
    Be sure your procedure works for the empty list.
        Examples:
          >>> my_sum([1,2,3,4])
          10
          >>> my_sum([3,5,10])
          18
    """
    pass


## 5: (Problem 1.7.5) Multiplying numbers in a list
def my_product(L):
    """
        Input:
          -L: a list of numbers
        Output:
          -the product of the numbers in L
    Be sure your procedure works for the empty list.
        Examples:
          >>> my_product([1,3,5])
          15
          >>> my_product([-3,2,4])
          -24
    """
    current = 1
    for num in L:
        current *= num
    return current


## 6: (Problem 1.7.6) Minimum of a list
def my_min(L):
    """
        Input:
          a list L of numbers
        Output:
          the minimum number in L
    Be sure your procedure works for the empty list.
    Hint: The value of the Python expression float('infinity') is infinity.
        Examples:
        >>> my_min([1,-100,2,3])
        -100
        >>> my_min([0,3,5,-2,-5])
        -5
    """
    pass


## 7: (Problem 1.7.7) Concatenation of a List
def my_concat(L):
    """
        Input:
          -L:a list of strings
        Output:
          -the concatenation of all the strings in L
    Be sure your procedure works for the empty list.
        Examples:
        >>> my_concat(['hello','world'])
        'helloworld'
        >>> my_concat(['what','is','up'])
        'whatisup'
    """
    current = ""
    for string in L:
        current += string
    return current


## 8: (Problem 1.7.8) Union of Sets in a List
def my_union(L):
    """
        Input:
          -L:a list of sets
        Output:
          -the union of all sets in L
    Be sure your procedure works for the empty list.
        Examples:
        >>> my_union([{1,2},{2,3}])
        {1, 2, 3}
        >>> my_union([set(),{3,5},{3,5}])
        {3, 5}
    """
    current = set()
    for a_set in L:
        for member in a_set:
            current.add(member)
    return current


## 9: (Problem 1.7.10) Complex Addition Practice
# Each answer should be a Python expression whose value is a complex number.

complex_addition_a = ...
complex_addition_b = ...
complex_addition_c = ...
complex_addition_d = ...


## 10: (Problem 1.7.12) Combining Complex Operations
# Write a procedure that evaluates ax+b for all elements in L


def transform(a, b, L):
    """
    Input:
      -a: a number
      -b: a number
      -L: a list of numbers
    Output:
      -a list of elements where each element is ax+b where x is an element in L
    Examples:
    >>> transform(3,2,[1,2,3])
    [5, 8, 11]
    """
    result = [a * num + b for num in L]
    return result


## 11: (Problem 1.7.13) GF(2) Arithmetic
GF2_sum_1 = ...  # answer with 0 or 1
GF2_sum_2 = ...
GF2_sum_3 = ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
