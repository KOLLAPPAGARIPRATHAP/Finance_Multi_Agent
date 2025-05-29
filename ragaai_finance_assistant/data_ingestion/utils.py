def format_percentage(value: float, decimals: int = 2) -> str:
    """
    Format a float as a percentage string.
    """
    try:
        return f"{value:.{decimals}f}%"
    except Exception:
        return "N/A"

def safe_float(value, default=0.0):
    """
    Convert a value to float safely.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

# Example usage:
if __name__ == "__main__":
    print(format_percentage(4.2567))  # Output: 4.26%
    print(safe_float("3.14"))          # Output: 3.14
    print(safe_float("abc"))           # Output: 0.0
