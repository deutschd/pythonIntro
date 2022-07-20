print("1. Pascal's triangle/recursion\n")


def pascals_triangle(n):
    """ Recursive function to calculate Pascals Triangle """
    if n == 1:
        return [[1]]  # Base case termination condition
    else:
        result = pascals_triangle(n - 1)  # Recursive call
        # Calculate current row using info from previous row
        current_row = [1]
        previous_row = result[-1]  # Take from end of result
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row += [1]
        result.append(current_row)
        return result


triangle = pascals_triangle(5)
for row in triangle:
    print(row)

print("\n1.1 Pascal's triangle:")


def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n - 1)
        last_row = result[-1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row += [1]
        result.append(new_row)
    return result


print(triangle(4))

print("\n1.2 Pascal's triangle:")

trianglex = lambda h: (lambda x: x + [[x + y for x, y in zip(x[-1] + [0], [0] + x[-1])]])(
    trianglex(h - 1)) if h > 1 else [[1]]
print(trianglex(3))

print("\n2.")
