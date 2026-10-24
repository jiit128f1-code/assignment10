
# Code Smell Inventory

| Smell name | Function and line numbers | Why it hurts | Refactoring to apply |
|---|---|---|---|
| Duplicated code | calc and calc2, lines 5-14 and 31-40 | Same slab calculations appear twice | Extract shared slab calculation |
| Long method | calc, lines 3-27 | Printing, calculation and validation are mixed | Extract smaller functions |
| Magic numbers | calc and calc2, rate and tax expressions | Business rules are difficult to identify | Introduce named constants |
| Unclear names | Both functions, parameters n, a, u, t, p, f | Readers cannot understand parameter meaning easily | Rename parameters |
| Comments standing in for names | Both function signatures | Comments are needed to explain short parameter names | Use descriptive names |
| Unused variable | calc, temp assignment | The result is never used | Remove dead code |
| Function doing two jobs | calc, printing and calculating | Calculation cannot be reused without printing | Separate calculation and output |
| Primitive flag | calc and calc2, parameter f | The senior flag's meaning is unclear | Rename to senior_flag |
| Repeated conditional logic | Both functions, connection type checks | Changes must be made in multiple places | Share calculation logic |
| Repeated slab arithmetic | Both functions, H and C branches | Rate tiers are implemented separately | Parameterize slab rates |
