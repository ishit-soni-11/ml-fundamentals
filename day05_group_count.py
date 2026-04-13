def group_count(data, col):
    counts={}
    for i in data:
        values=i[col]
        if values in counts:
            counts[values]+=1
        else:
            counts[values]=1
    return counts







data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'Toronto'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Calgary'},
    {'Name': 'Charlie', 'Age': '35', 'City': 'Calgary'},
    {'Name': 'Dana', 'Age': '28', 'City': 'Toronto'},
    {'Name': 'Eve', 'Age': '40', 'City': 'Vancouver'}
]
col="City"

print(group_count(data,col))