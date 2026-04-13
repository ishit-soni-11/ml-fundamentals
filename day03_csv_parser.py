def parse_csv(filepath):
    with open(filepath, "r") as file:
        ReadAllLines = file.readlines()
        Result = []
        Header = ReadAllLines[0].strip().split(",")
        for line in ReadAllLines[1:]:
            row_data = {}
            values = line.strip().split(",")
            for i in range(len(Header)):
                row_data[Header[i]] = values[i]
            Result.append(row_data)
    return Result

# Test
print(parse_csv('/Users/ishit/Documents/ML/Python/CSV/sample.csv'))