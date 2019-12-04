def generate_id(vendor):
    from random import seed, randint

    prefix = {'AMEX': '37', 'MASTERCARD': '55', 'VISA': '4'}
    length = {'AMEX': 15, 'MASTERCARD': 16, 'VISA': 16}

    # Initialize the id with the vendor's prefix
    id = prefix[vendor]

    # Every number other than the prefix and the least significant
    # digit is generated randomly
    for i in range(length[vendor] - len(id) - 1):
        seed()
        id += str(randint(0, 9))

    # Calculate the last digit (check digit) as the digit that
    # makes the summation in luhn's algorithm a multiple of 10
    summation = sum([int(n) if i % 2 else sum([int(m) for m in str(int(n) * 2)]) for i, n in enumerate(reversed(id))])
    check_digit = (10 - (summation % 10)) % 10

    # Concatenate the check digit and return the id
    return id + str(check_digit)

# Validates whether the given id is a valid credit card ID or not without
# the need of a database connection
def validate_id(id):
    # Initialize luhn's summation to be zero
    summation = 0

    # Check if the summation of luhn's algorithm is modulo 10
    for i, n in enumerate(reversed(id)):
        digit = sum([int(m) for m in str(int(n) * 2)]) if i % 2 else int(n)
        summation += digit

    return True if summation % 10 == 0 else False
    
