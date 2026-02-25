#!/usr/bin/env python3

import sys
import os
import site


def main() -> None:
    # Compare prefix with base_prefix. If identical no venv is active
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print("\nThen run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        site_dirs = site.getsitepackages()
        # Filter for site-packages, excluding dist-packages
        for site_dir in site_dirs:
            if "site-packages" in site_dir:
                print(site_dir)
                break


if __name__ == "__main__":
    main()
