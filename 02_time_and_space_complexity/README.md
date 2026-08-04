
# Phase 2: Time & Space Complexity

| Phase | Topic                                    |     Status    | Notes                                                             |
| ----: | ---------------------------------------- | :-----------: | ----------------------------------------------------------------- |
|     1 | Why Complexity Matters                   | ❌ Not Started | Understand why algorithms are measured instead of execution time. |
|     2 | Time Complexity Basics                   | ❌ Not Started | Learn how operations grow as input size increases.                |
|     3 | Big-O Notation (Worst Case)              | ❌ Not Started | Most commonly used notation in interviews.                        |
|     4 | Big-Theta (Average Case)                 | ❌ Not Started | Exact asymptotic bound.                                           |
|     5 | Big-Omega (Best Case)                    | ❌ Not Started | Lower bound of algorithm performance.                             |
|     6 | Common Time Complexities                 | ❌ Not Started | O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!).            |
|     7 | Complexity of Single Loop                | ❌ Not Started | Analyze simple iterative algorithms.                              |
|     8 | Complexity of Nested Loops               | ❌ Not Started | Analyze multiple nested iterations.                               |
|     9 | Complexity of Logarithmic Loops          | ❌ Not Started | `i *= 2`, `i /= 2`, binary-style loops.                           |
|    10 | Complexity of Multiple Independent Loops | ❌ Not Started | Sequential loops and combined complexity.                         |
|    11 | Complexity of Conditional Statements     | ❌ Not Started | `if`, `if-else`, and branching analysis.                          |
|    12 | Complexity of Recursive Functions        | ❌ Not Started | Build recurrence relations.                                       |
|    13 | Recursion Stack Space                    | ❌ Not Started | Understand implicit memory usage.                                 |
|    14 | Master's Theorem (Basics)                | ❌ Not Started | Solve divide-and-conquer recurrences.                             |
|    15 | Space Complexity Basics                  | ❌ Not Started | Auxiliary Space vs Total Space.                                   |
|    16 | Time vs Space Trade-off                  | ❌ Not Started | Optimize based on constraints.                                    |
|    17 | Amortized Analysis                       | ❌ Not Started | Dynamic array growth and average cost.                            |
|    18 | Complexity of Python Built-in Operations | ❌ Not Started | Lists, dictionaries, sets, strings, heaps, etc.                   |
|    19 | Complexity of Sorting Algorithms         | ❌ Not Started | Compare Bubble, Merge, Quick, Heap, etc.                          |
|    20 | Complexity Analysis Practice             | ❌ Not Started | Analyze complete algorithms and code snippets.                    |


# Practice Checklist

After completing the theory, solve these in order.

| No. | Practice Problem                       | Status |
| --: | -------------------------------------- | :----: |
|   1 | Find complexity of a single loop       |    ❌   |
|   2 | Find complexity of nested loops        |    ❌   |
|   3 | Find complexity of logarithmic loops   |    ❌   |
|   4 | Find complexity of mixed loops         |    ❌   |
|   5 | Find complexity of recursive Fibonacci |    ❌   |
|   6 | Find complexity of Binary Search       |    ❌   |
|   7 | Solve Merge Sort recurrence            |    ❌   |
|   8 | Compare O(n log n) vs O(n²)            |    ❌   |
|   9 | Identify recursion stack space         |    ❌   |
|  10 | Analyze Python built-in operations     |    ❌   |
|  11 | Analyze HashMap complexity             |    ❌   |
|  12 | Analyze Dynamic Array append           |    ❌   |



# Common Complexity Reference

| Complexity | Name         | Typical Example          |
| ---------- | ------------ | ------------------------ |
| O(1)       | Constant     | Array index, Hash lookup |
| O(log n)   | Logarithmic  | Binary Search            |
| O(√n)      | Square Root  | Prime checking           |
| O(n)       | Linear       | Single Loop              |
| O(n log n) | Linearithmic | Merge Sort, Heap Sort    |
| O(n²)      | Quadratic    | Two Nested Loops         |
| O(n³)      | Cubic        | Three Nested Loops       |
| O(2ⁿ)      | Exponential  | Recursive Subsets        |
| O(n!)      | Factorial    | Permutations             |


This mirrors how you'll actually reason during interviews:

1. Identify the loops or recursion.
2. Estimate the time complexity.
3. Estimate the space complexity.
4. Explain any trade-offs.
