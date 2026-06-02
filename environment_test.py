"""
environment_test.py
Lab 0 - Environment Verification Script

This script checks whether the Python environment is ready for the AI lab.
It verifies the Python version, operating system, required packages,
and whether a virtual environment is active.
"""

import sys
import platform
import os


def verify_environment():
    """Check Python version, OS, installed packages, and active environment."""

    results = []

    # Check Python version
    python_version = sys.version.split()[0]
    results.append(f"Python Version: {python_version}")

    # Check operating system
    operating_system = platform.system()
    os_release = platform.release()
    results.append(f"Operating System: {operating_system} {os_release}")

    # Check required packages
    required_packages = {
        "numpy": "NumPy",
        "pandas": "Pandas",
        "matplotlib": "Matplotlib",
        "sklearn": "Scikit-learn"
    }

    for package_name, display_name in required_packages.items():
        try:
            module = __import__(package_name)
            version = getattr(module, "__version__", "unknown")
            results.append(f"{display_name}: Installed, version {version}")
        except ImportError:
            results.append(f"{display_name}: Not installed")

    # Check whether a virtual environment is active
    in_virtual_environment = sys.prefix != sys.base_prefix

    if in_virtual_environment:
        results.append(f"Virtual Environment: Active ({sys.prefix})")
    elif "CONDA_PREFIX" in os.environ:
        results.append(f"Conda Environment: Active ({os.environ['CONDA_PREFIX']})")
    else:
        results.append("Virtual Environment: Not active")

    return "\n".join(results)


if __name__ == "__main__":
    print("=" * 50)
    print("LAB 0: ENVIRONMENT VERIFICATION")
    print("=" * 50)
    print(verify_environment())
    print("=" * 50)