# Python
## Modules
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
- `math.factorial(n)`: First, it exists. Accepts only nonneg ints. No negatives and floats including e.g. (3.0).

## Shortcuts
- c++ print array
```cpp
for (auto &i: arr) cout << i << ' ';
```

# Algorithms
## Geometry
### Convex Hull
- Number of vertices(range: N) in Convex Hull is ~O(N^(2/3))
