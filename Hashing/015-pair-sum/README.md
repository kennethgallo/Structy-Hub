## pair sum

Write a function, *pair_sum*, that takes in a list and a target sum as arguments. The function
should return a tuple containing a pair of indices whose elements sum to the given target. The
indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

#### test_00:

```python
pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
```

#### test_01:

```python
pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
```

#### test_02:

```python
pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
```

#### test_03:

```python
pair_sum([1, 6, 7, 2], 13) # -> (1, 2)
```

#### test_04:

```python
pair_sum([9, 9], 18) # -> (0, 1)
```

#### test_05:

```python
pair_sum([6, 4, 2, 8 ], 12) # -> (1, 3)
```

#### test_06:

```python
numbers = [ i for i in range(1, 6001) ]
pair_sum(numbers, 11999) # -> (5998, 5999)
```
