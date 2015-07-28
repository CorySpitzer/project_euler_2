# def find_sum():

def is_even(integer):
    return integer % 2 == 0

class FibonacciSequence:
    def even_sum(self):
        small_int = 1
        big_int = 2
        sum = 0
        while big_int < int(4e6): # 4 million
            if is_even(big_int):
                sum += big_int
            small_int, big_int = big_int, big_int + small_int
        return sum
