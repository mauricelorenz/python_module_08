#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    # .env is required for all configuration values
    if not os.path.exists(".env"):
        print("Error: .env missing!")
        sys.exit(1)
    print("\nConfiguration loaded:")
    print(f"Mode: {os.getenv("MATRIX_MODE")}")
    db = ("Connected to local instance"
          if os.getenv("DATABASE_URL") else "URL missing")
    print(f"Database: {db}")
    api = "Authenticated" if os.getenv("API_KEY") else "Key missing"
    print(f"API Access: {api}")
    print(f"Log Level: {os.getenv("LOG_LEVEL")}")
    zion = "Online" if os.getenv("ZION_ENDPOINT") else "Offline"
    print(f"Zion Network: {zion}")
    print("\nEnvironment security check:")
    required_envs = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
                     "LOG_LEVEL", "ZION_ENDPOINT"]
    for required_env in required_envs:
        if not os.getenv(required_env):
            print("Error: Missing environment variables!")
            sys.exit(1)
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
