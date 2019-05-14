def convolution(x, k):
    # Convolution function

    # The variable result is the matrix to return
    result = []

    # Function calculating root square
    # Naive implementation because it is only called with perfect squares
    def square_root(n):
        i = 0
        while i * i < n:
          i += 1
        return i

    # Compute the matrice orders (base matrix and kernel matrix)
    order_x = square_root(len(x))
    order_k = square_root(len(k))

    # Check if the kernel order is odd
    if order_k % 2 == 0:
        return result

    # We need to find the center of the matrix to transform in order to compute the indexes during matrices superposition
    center = order_k // 2

    # Browse lines of the base matrix
    for i in range(order_x):

        # Browse columns of the base matrix
        for j in range(order_x):

            # Define the variable that is going to contain the indexes sum for les the new values to add in the new matrix
            sum_index = 0

            # Browse lines of the kernel matrix
            for l in range(order_k):

                # Browse columns of the kernel matrix
                for m in range(order_k):

                    # Compute lines index for matrix x
                    index_row = i + center - order_k + 1 + l

                    # Compute columns index for matrix x
                    index_col = j + center - order_k + 1 + m

                    # Check to know if the current indexes are out of bound of the matrix
                    if index_row >= 0 and index_row < order_x and index_col >= 0 and index_col < order_x:

                        # Formula that adds the products sum of neighboor values and of the current cell
                        sum_index += x[index_row * order_x + index_col] * k[l * order_k + m]

            # We add the new cell to the new matrix containing the new values after the convolution
            result.append(sum_index)

    # We return the new matrix, it has the same order as the input matrix
    return result
