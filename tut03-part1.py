def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_rotations(num):
    rotations = []
    num_str = str(num)
    for i in range(len(num_str)):
        rotation = num_str[i:] + num_str[:i]
        rotations.append(int(rotation))
    return rotations

def is_rotational_prime(num):
    rotations = generate_rotations(num)
    for rotation in rotations:
        if not is_prime(rotation):
            return False
    return True

number = input('Enter a number: ')
number = int(number)
if is_rotational_prime(number):
    print(f"{number} is a rotational prime.")
else:
    print(f"{number} is not a rotational prime.")