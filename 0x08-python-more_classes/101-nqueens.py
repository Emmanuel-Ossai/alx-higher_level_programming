#!/usr/bin/python3

"""
The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard.
"""


from sys import argv


def find_nqueens(n):
    """
    Check the coordinates of N queens in non-attacking positions
    on an NxN grid

    Args:
        n (int): The size of the grid and the number of queens.

    Raises:
        ValueError: If n is less than 4.

    """
    if n < 4:
        raise ValueError("N must be at least 4")

    a = []

    # Initialize the answer list
    for i in range(n):
        a.append([i, None])

    def already_exists(l):
        """
        Check if a queen already exists at the given y-coordinate.

        Args:
            l (int): The y-coordinate to check.

        Returns:
            bool: True if a queen exists

        """
        for k in range(n):
            if l == a[k][1]:
                return True
        return False

    def reject(k, l):
        """
        Determine whether to reject the solution.

        Args:
            k (int): The current x-coordinate.
            l (int): The current y-coordinate.

        Returns:
            bool: True if the solution should be rejected, False otherwise.

        """
        if already_exists(l):
            return False
        i = 0
        while i < k:
            if abs(a[i][1] - l) == abs(i - k):
                return False
            i += 1
        return True

    def clear_a(k):
        """
        Clear the answers from the point of failure onwards.

        Args:
            k (int): The x-coordinate to start clearing from.

        """
        for i in range(k, n):
            a[i][1] = None

    def solve_nqueens(k):
        """
        Recursive backtracking function to find the solution.

        Args:
            k (int): The current x-coordinate.

        """
        for l in range(n):
            clear_a(k)
            if reject(k, l):
                a[k][1] = l
                if k == n - 1:  # Accepts the solution
                    print(a)
                else:
                    solve_nqueens(k + 1)  # Move on to the next x-coordinate to continue

    # Start the recursive process at x = 0
    solve_nqueens(0)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    find_nqueens(n)
