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

def group_count(data, col):
    counts={}
    for i in data:
        values=i[col]
        if values in counts:
            counts[values]+=1
        else:
            counts[values]=1
    return counts



# ---- PIPELINE ----
# Step 1: Load the CSV
data = parse_csv('/Users/ishit/Documents/ML/Python/CSV/sample.csv')

# Step 2: Filter rows where Age > 27
filtered = []
for row in data:
    if int(row['Age']) > 27:
        filtered.append(row)

# Step 3: Group filtered data by City
result = group_count(filtered, 'City')

# Step 4: Print the result
print(result)