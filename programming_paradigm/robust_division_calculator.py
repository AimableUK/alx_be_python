def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        return num / den

    except ValueError:
        return "Please provide numbers ONLY!"

    except ZeroDivisionError:
        return "You can't divide a number with zero"
