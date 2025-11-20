def perform_operation(numb1, numb2, operation):
    numb1 = float(numb1)
    numb2 = float(numb2)
    operation = str(operation)
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

