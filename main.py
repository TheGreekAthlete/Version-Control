def encode(password):
    return ''.join([str(int(item) + 3) for item in password])

def decode(password):
    return ''.join([str(int(item) - 3) for item in password])

