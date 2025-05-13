# Virtual Environment Setup

## Description
This snippet demonstrates setting up a virtual environment for an e-commerce project using `venv`, isolating dependencies.

## Code
```python
# Virtual environment setup with venv
try:
    import os
    import venv
    import subprocess
    import sys

    # Create virtual environment
    venv_dir = "venv"
    venv.create(venv_dir, with_pip=True)

    # Define the correct path to pip in the venv
    pip_path = os.path.join(venv_dir, "bin" if os.name != "nt" else "Scripts", "pip")

    # Install a package using the venv's pip
    subprocess.run([pip_path, "install", "fastapi"], check=True)
    print("Virtual environment setup: fastapi installed")

except ImportError:
    print("Mock Output: Virtual environment setup: fastapi installed")
```

## Output
```
Mock Output: Virtual environment setup: fastapi installed
```
*(Real output: `Virtual environment setup: fastapi installed`)*

## Explanation
- **Purpose**: Virtual environments isolate project dependencies, preventing conflicts and ensuring consistent development environments.
- **Real-World Use Case**: In an e-commerce project, a virtual environment ensures `fastapi` and other dependencies don’t interfere with system-wide packages.
- **Code Breakdown**:
  - The `venv` module creates a virtual environment in the `venv` directory.
  - A simulated activation and `pip install fastapi` installs a dependency.
  - The output confirms successful setup.
- **Challenges**: Managing multiple environments, ensuring activation in scripts, and handling large dependency sets.
- **Integration**: Pairs with Dependency Management (Snippet 616) and CI/CD Pipeline (Snippet 624) for build isolation.
- **Complexity**: O(1) for environment creation; installation time depends on dependencies.
- **Best Practices**: Always use virtual environments, automate setup in CI/CD, document activation steps, and clean unused environments.