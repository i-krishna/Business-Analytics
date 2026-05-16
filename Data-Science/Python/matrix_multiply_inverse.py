"""
Data Compute vs AI Compute

Data compute (Spark, Trino, Snowflake) moves data through CPUs to answer queries. The bottleneck here is moving data — from disk to memory to CPU and back (I/O-bound work). The CPU cores are doing relatively simple operations (comparisons, additions, string matches) but on billions of rows. The parallelism is horizontal — you add more machines to handle more data. Each machine has regular CPUs (like Intel Xeon or AMD EPYC). The work is sequential per row but distributed across thousands of rows simultaneously.
AI compute (A100, H100, L40) moves numbers through thousands of GPU cores simultaneously to train or run models. Training a neural network or running inference is a completely different kind of work. At its core, everything in AI reduces to one operation repeated billions of times: matrix multiplication.
A simple neural network layer does this:
output = input_matrix × weight_matrix + bias
Where input_matrix might be shape [batch_size=512, features=4096] and weight_matrix is [4096, 4096]. That's 512 × 4096 × 4096 = 8.5 billion multiply-and-add operations — for a single layer, for a single forward pass.
A CPU does this sequentially across its 16-64 cores. An A100 GPU has 6,912 CUDA cores all running simultaneously, specifically designed to do matrix math in parallel. That's why the same operation takes seconds on a CPU and milliseconds on a GPU.
"""
import numpy as np

class BlockDiagonalMatrix:
    def __init__(self, n, d):
        self.n = n  # Number of blocks per row/column
        self.d = d  # Size of each block
        self.blocks = {}  # Dictionary to store diagonal blocks

    def set_block(self, i, j, diag):
        """Set the diagonal elements of block (i, j)."""
        if len(diag) != self.d:
            raise ValueError("Diagonal size must be equal to block size.")
        self.blocks[(i, j)] = np.array(diag)

    def multiply(self, other):
        """Multiply with another BlockDiagonal Matrix."""
        if self.n != other.n or self.d != other.d:
            raise ValueError("Matrix dimensions must match.")

        result = BlockDiagonalMatrix(self.n, self.d)

        for i in range(self.n):  # Loop over rows of result
            for j in range(self.n):  # Loop over columns of result
                block_result = np.zeros(self.d)  # Initialize the block (i, j) as zero
                for k in range(self.n):  # Loop over the blocks to compute dot product
                    D_ik = self.blocks.get((i, k), np.zeros(self.d))  # Get block (i, k)
                    D_kj = other.blocks.get((k, j), np.zeros(self.d))  # Get block (k, j)
                    block_result += D_ik * D_kj  # Multiply diagonal elements and sum
                if np.any(block_result != 0):  # Add the block to the result only if non-zero
                    result.set_block(i, j, block_result)

        return result

    def inverse(self):
        """Compute the inverse of the matrix."""
        result = BlockDiagonalMatrix(self.n, self.d)
        for (i, j), diag in self.blocks.items():
            if i != j:
                raise ValueError("Only diagonal blocks can be inverted.")
            if np.any(diag == 0):
                raise ValueError("Singular block detected.")
            result.set_block(i, j, 1.0 / diag)  # Invert each diagonal element
        return result

    def display(self):
        """Display the full matrix."""
        full_matrix = np.zeros((self.n * self.d, self.n * self.d))
        for (i, j), diag in self.blocks.items():
            for k in range(self.d):
                full_matrix[i * self.d + k, j * self.d + k] = diag[k]
        print(full_matrix)

if __name__ == "__main__":
    n, d = 3, 3  # 3 blocks, each 3x3
    A = BlockDiagonalMatrix(n, d)
    A.set_block(0, 0, [1, 2, 3])
    A.set_block(1, 1, [4, 5, 6])
    A.set_block(2, 2, [7, 8, 9])

    print("Matrix A:")
    A.display()

    print("\nMatrix A Inverse:")
    A_inv = A.inverse()
    A_inv.display()
