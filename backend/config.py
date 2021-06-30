import os


def get_var(var_name: str) -> str:
    """Get environment variable value."""
    return os.getenv(var_name.upper())
