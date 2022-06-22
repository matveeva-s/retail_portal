def round_with_precision(number, precision=3):
    return f"{number:.{precision}f}" if number else None