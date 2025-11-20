def perform_operation(numb1: float, numb2: float, operation: str):
    operation = operation.lower()
    
    if operation == "add":
        return numb1 + numb2
    elif operation == "subtract":
        return numb1 - numb2
    elif operation == "multiply":
        return numb1 * numb2
    elif operation == "divide":
        if numb2 == 0:
            return "Error: Division by zero"
        return numb1 / numb2
    else:
        return "Error: Invalid operation"
