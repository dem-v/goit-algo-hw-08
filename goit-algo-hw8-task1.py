# Python3 program to connect n
# ropes with minimum cost
# https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
import heapq


def min_cost(arr: list, n: int):
    # arr - list of given rope lengths
    # n - number of ropes to connect
    heapq.heapify(arr)

    max_rope_count = min(len(arr), n) if n>0 and len(arr)>0 else 0

    # Initialize result
    res = 0

    # While size of priority queue is more than 1
    while (len(arr) > 1) and max_rope_count > 0:
        # Extract shortest two ropes from arr
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)

        # Connect the ropes: update result
        # and insert the new rope to arr
        res += first + second
        heapq.heappush(arr, first + second)
        max_rope_count -= 1

    return res


# Driver code
if __name__ == '__main__':
    lengths = [4, 3, 2, 6, 10, 12, 14, 15]
    size = 3  # len(lengths)

    print("Total cost for connecting ropes is " +
          str(min_cost(lengths, size)))
