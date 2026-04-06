import numpy as np

def calculate(numbers):
    # Check if the list has exactly 9 elements
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 NumPy array
    matrix = np.array(numbers).reshape(3, 3)
    
    # Prepare calculations
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # mean of columns
            matrix.mean(axis=1).tolist(),  # mean of rows
            matrix.mean().item()           # mean of all elements
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }
    
    return calculations

# ======= Testing the function =======
if __name__ == "__main__":
    # Sample input
    numbers = [0,1,2,3,4,5,6,7,8]

    # Call calculate function
    result = calculate(numbers)

    # Print results
    for key, value in result.items():
        print(f"{key}: {value}")
