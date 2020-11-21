
row = [square for square in input()]
colours = ['R','G','B']



while len(row) > 1:
    new_row = []
    for i in range(len(row) - 1):
        if row[i] == row [i+1]:
            new_row.append(row[i])
        else:
            new_row.extend([colour for colour in colours if colour != row[i] and colour != row[i+1]])
    row = new_row

print("".join(row))


