def sort_column_bubble(matrix, col):
    n = len(matrix)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if matrix[j][col] > matrix[j-1][col]:
                matrix[j][col], matrix[j-1][col] = matrix[j-1][col], matrix[j][col]

def sort_matrix(matrix):
    cols = len(matrix[0])
    for col in range(cols):
        sort_column_bubble(matrix, col)
    return matrix

def calculate_fi(matrix):
    n = len(matrix)
    m = len(matrix[0])
    results = []
    
    for i in range(n):
        product = 1
        count = 0
        for j in range(m):
            if i + j > n - 1:
                product *= matrix[i][j]
                count += 1
        
        if count > 0:
            results.append(product)
        else:
            results.append(0)
    
    return results

def calculate_F(fi_values):
    if len(fi_values) == 0:
        return 0
    return sum(fi_values) / len(fi_values)

def print_matrix(matrix, title="Matrix:"):
    print(title)
    for row in matrix:
        print([f"{x:4}" for x in row])
    print()

A = [
    [-1, -5, -47, -8, -1],
    [-4, -98, -90, -45, -78],
    [-3, -2, -5, -9, -4],
    [-8, -67, -33, -91, -40],
    [-2, -58, -11, -65, -77]
]

print_matrix(A, "Original matrix:")

sort_matrix(A)
print_matrix(A, "Sorted matrix (columns descending):")

fi_values = calculate_fi(A)
print("f_i values (product of elements below auxiliary diagonal for each row):")
for i, val in enumerate(fi_values):
    print(f"f_{i+1} = {val}")

F_value = calculate_F(fi_values)
print(f"\nF value (arithmetic mean of f_i): {F_value:.2f}")