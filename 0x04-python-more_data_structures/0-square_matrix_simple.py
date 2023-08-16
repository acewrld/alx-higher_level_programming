def square_matrix_simple(matrix=[]):
    # Create an empty matrix to store the squared values
    result_matrix = []
    
    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []
        
        # Iterate through each element in the current row
        for element in row:
            # Square the element and add it to the result row
            result_row.append(element ** 2)
        
        # Add the result row to the result matrix
        result_matrix.append(result_row)
    
    return result_matrix

