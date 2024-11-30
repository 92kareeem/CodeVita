class LetterMatrixTransformer:
    @staticmethod
    def main():
        input_manager = InputHandler()
        grid_size = input_manager.read_grid_size()
        letter_grid = input_manager.read_letter_matrix(grid_size)
        query_count = input_manager.read_query_count()

        query_handler = QueryProcessor()
        for _ in range(query_count):
            query_params = input_manager.read_query_parameters()
            query_handler.execute_rotation(letter_grid, query_params[0], query_params[1], query_params[2])

        LetterMatrixTransformer.display_final_matrix(letter_grid)

    @staticmethod
    def display_final_matrix(letter_matrix):
        output_builder = []
        for row in letter_matrix:
            output_builder.extend(row)
        print(''.join(output_builder))


class QueryProcessor:
    def execute_rotation(self, matrix, base_row, base_col, submatrix_size):
        layer_depth = submatrix_size // 2
        for current_layer in range(layer_depth):
            self.perform_layer_rotation(matrix, base_row, base_col, submatrix_size, current_layer)

    def perform_layer_rotation(self, matrix, base_row, base_col, submatrix_size, layer):
        border_elements = self.extract_border_elements(matrix, base_row, base_col, submatrix_size, layer)
        rotation_factor = layer + 1
        transformed_elements = self.transform_element_sequence(border_elements, rotation_factor)
        self.update_matrix_border(matrix, base_row, base_col, submatrix_size, layer, transformed_elements)

    def extract_border_elements(self, matrix, base_row, base_col, size, layer):
        elements = []
        start_row = base_row + layer
        end_row = base_row + size - 1 - layer
        start_col = base_col + layer
        end_col = base_col + size - 1 - layer

        # Top row (left to right)
        for i in range(start_col, end_col + 1):
            elements.append(matrix[start_row][i])

        # Right column (top to bottom)
        for i in range(start_row + 1, end_row):
            elements.append(matrix[i][end_col])

        # Bottom row (right to left)
        for i in range(end_col, start_col - 1, -1):
            elements.append(matrix[end_row][i])

        # Left column (bottom to top)
        for i in range(end_row - 1, start_row, -1):
            elements.append(matrix[i][start_col])

        return elements

    def transform_element_sequence(self, sequence, rotation_index):
        effective_rotation = rotation_index % len(sequence)
        if rotation_index % 2 == 1:
            # Rotate left for odd rotations
            sequence = sequence[effective_rotation:] + sequence[:effective_rotation]
            # Shift letters backward (counter-clockwise)
            return [self.shift_letter_backward(symbol) for symbol in sequence]
        else:
            # Rotate right for even rotations
            sequence = sequence[-effective_rotation:] + sequence[:-effective_rotation]
            # Shift letters forward (clockwise)
            return [self.shift_letter_forward(symbol) for symbol in sequence]

    def update_matrix_border(self, matrix, base_row, base_col, size, layer, transformed_elements):
        start_row = base_row + layer
        end_row = base_row + size - 1 - layer
        start_col = base_col + layer
        end_col = base_col + size - 1 - layer

        element_index = 0

        # Top row (left to right)
        for i in range(start_col, end_col + 1):
            matrix[start_row][i] = transformed_elements[element_index]
            element_index += 1

        # Right column (top to bottom)
        for i in range(start_row + 1, end_row):
            matrix[i][end_col] = transformed_elements[element_index]
            element_index += 1

        # Bottom row (right to left)
        for i in range(end_col, start_col - 1, -1):
            matrix[end_row][i] = transformed_elements[element_index]
            element_index += 1

        # Left column (bottom to top)
        for i in range(end_row - 1, start_row, -1):
            matrix[i][start_col] = transformed_elements[element_index]
            element_index += 1

    def shift_letter_backward(self, symbol):
        # Shift letter backwards, wrap around 'A' to 'Z'
        return 'Z' if symbol == 'A' else chr(ord(symbol) - 1)

    def shift_letter_forward(self, symbol):
        # Shift letter forward, wrap around 'Z' to 'A'
        return 'A' if symbol == 'Z' else chr(ord(symbol) + 1)


class InputHandler:
    def read_grid_size(self):
        return int(input().strip())

    def read_letter_matrix(self, grid_size):
        letter_matrix = []
        for _ in range(grid_size):
            row_elements = input().strip().split()
            letter_matrix.append([char for char in row_elements])
        return letter_matrix

    def read_query_count(self):
        return int(input().strip())

    def read_query_parameters(self):
        query_details = input().strip().split()
        return [int(x) for x in query_details]


# To execute the program
if __name__ == '__main__':
    LetterMatrixTransformer.main()
