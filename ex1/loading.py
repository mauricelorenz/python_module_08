#!/usr/bin/env python3

import sys
import importlib
import importlib.metadata
try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    to_import = ["pandas", "matplotlib", "numpy"]
    not_available = []
    # Check which dependencies are missing
    for module in to_import:
        try:
            importlib.import_module(module)
        except ImportError:
            not_available += [module]
    print(f"Missing dependencies: {not_available}")
    print("pip: Run pip install -r requirements.txt && python3 "
          "loading.py\n"
          "Poetry: Run poetry install && poetry run python loading.py")
    sys.exit()


def check_dependencies() -> None:
    print("\nChecking dependencies:")
    print(f"[OK] pandas ({importlib.metadata.version("pandas")}) - "
          "Data manipulation ready")
    print(f"[OK] matplotlib ({importlib.metadata.version("matplotlib")}) - "
          "Visualization ready")
    print(f"[OK] numpy ({importlib.metadata.version("numpy")}) - "
          "Calculation ready")


def analyze_matrix_data() -> np.ndarray:
    print("\nAnalyzing Matrix data...")
    matrix_data = np.random.normal(loc=0, scale=1, size=1000)
    print(matrix_data)
    print()
    return matrix_data


def process_data_points(matrix_data: np.ndarray) -> pd.Series:
    print("Processing 1000 data points...")
    matrix_series = pd.Series(matrix_data)
    print(matrix_series.describe())
    print()
    return matrix_series


def generate_visualization(matrix_series: pd.Series) -> None:
    print("Generating visualization...")
    plt.hist(matrix_series)
    filename = "matrix_analysis.png"
    plt.savefig(filename)
    print("\nAnalysis complete!")
    print(f"Results saved to: {filename}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    check_dependencies()
    matrix_data = analyze_matrix_data()
    matrix_series = process_data_points(matrix_data)
    generate_visualization(matrix_series)


if __name__ == "__main__":
    main()
