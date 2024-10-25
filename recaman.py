L = int(input("Length of sequence: "))  # this should be your only input

sequence = [0]

# Generate the sequence
for k in range(1, L):
    next_value = sequence[-1] - k  # Calculate ak-1 - k
    if next_value > 0 and next_value not in sequence:
        sequence.append(next_value)
    else:
        sequence.append(sequence[-1] + k)  # use ak-1 + k

# Final output
[print(sequence)]
