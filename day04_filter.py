def parse_csv(filepath):
    with open(filepath,"r") as file:
        ReadAllLines=file.readlines()
        Result=[]
        Header=ReadAllLines[0].strip().split(",") # first part of list that is column
    
        for line in ReadAllLines[1:]:
            row_data={}
            values=line.strip().split(",")
            for i in range(len(Header)):
                row_data[Header[i]] = values[i]
            Result.append(row_data)
    return Result

def filter_data(data, col, val):
    Result=[]
    for row in data:
        if row[col]==val:
            Result.append(row)
    return Result
# Test data
data = parse_csv('/Users/ishit/Documents/ML/Python/CSV/sample.csv')

print(filter_data(data, 'Name', 'Alice'))
print(filter_data(data, 'Age', '30'))

