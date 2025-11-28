  
def safe_divide(numerator, denominator):
    try: 
        numerator != 0
        denominator != 0
    except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
            return "Error: Please enter numeric values."
      