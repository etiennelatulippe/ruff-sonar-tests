# Getting started

- Launch the devcontainer
- Create a token on http://localhost:9000 (default user/password is admin:admin)
- Copy the token in .devcontainer/devcontainer.json


# How to run tests:

With Ruff (forced to 5 to trigger an error)

- `ruff check`

output:

```sh
src/mycomplexfunction.py:1:5: C901 `another_function` is too complex (6 > 5)
  |
1 | def another_function(y):
  |     ^^^^^^^^^^^^^^^^ C901
2 |     if y > 0:
3 |         for i in range(y):
  |
```

- `pysonar-scanner`

output from the web:

```sh
src/mycomplexfunction.py
Refactor this function to reduce its Cognitive Complexity from 18 to the 15 allowed.
9 locations

...
```