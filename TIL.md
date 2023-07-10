# Python
## Syntax

- `A = [input() for _ in range(int(input()))]` works in a single line, as the latter `input()` goes first.

- `:=` (walrus) operator: Assignment exprsesion operator. (New in Python 3.8)
```Python
# Handle a matched regex
if (match := pattern.search(data)) is not None:
    # Do something with match

# A loop that can't be trivially rewritten using 2-arg iter()
while chunk := file.read(8192):
   process(chunk)

# Reuse a value that's expensive to compute
[y := f(x), y**2, y**3]

# Share a subexpression between a comprehension filter clause and its output
filtered_data = [y for x in data if (y := f(x)) is not None]
```

## Module
### built-in modules

- `int(n, base)`: `n` can be a string, and also doesn't have to be in a proper base format.
```Python
print(int("101", 2)) # 5
```

- `filter(function, sequence)`
  - `function`: function that tests if each element of a sequence is true or not.
  - `sequence`: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
  - Returns: an iterator that is already filtered.
```Python
result = list(filter(lambda x: is_multiple_of_3(x), numbers))
print(result) # [3, 6, 9]
```

### `math` module

- `math.dist(p, q)`: Return the Euclidean distance between two points p and q, each given as a sequence (or iterable) of coordinates. The two points must have the same dimension. Roughly equivalent to:
```python
sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
```

- `math.hypot(*coordinates)`: Return the Euclidean norm, `sqrt(sum(x**2 for x in coordinates))`. This is the length of the vector from the origin to the point given by the coordinates.
```python
# Euclidean norm
# sqrt(x1*x1 + x2*x2 +x3*x3 .... xn*xn)
math.hypot(x1, x2, x3, ..., xn)
```

- `math.factorial(n)`: Accepts only a nonneg int. No negatives and floats including e.g. (3.0).

## Shortcuts

- c++ print array
```cpp
for (auto &i: arr) cout << i << ' ';
```

# Algorithms
## Geometry
### Convex Hull
- Number of vertices(range: $N$) in Convex Hull is $\sim O(N^{\frac{2}{3}})$
