def square_sum(c: int) -> bool:
    factor = 2

    # scan each prime factor
    while factor * factor <= c:
        print(f'factor: {factor}')
        exponent_of_factor = 0

        # check whether " factor | c " or not
        if c % factor == 0:
            print(f'c % factor = 0')
            # get the exponent of current factor
            while c % factor == 0:
                # accumulate the exponenet of prime factor
                exponent_of_factor += 1
                print(f'exponent_of_factor: {exponent_of_factor}')

                # update c
                print(f'c = c // factor = {c} // {factor} = {c // factor}')
                c = c // factor

            # Reject factor decomposition in the form: " (4k+3)^q | c ", where q is odd integer
            if factor % 4 == 3 and exponent_of_factor % 2 != 0:
                return False

        # try next factor
        factor += 1

    # Reject number in the form: c = 4k+3 where k is non-negative integer
    return c % 4 != 3


print(square_sum(100000))