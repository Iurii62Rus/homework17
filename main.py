def calculate_structure_sum(*args):
    def process_element(element):
        total = 0
        if isinstance(element, int):
            total += element
        elif isinstance(element, str):
            total += len(element)
        elif isinstance(element, (list, tuple)):
            for item in element:
                total += process_element(item)
        elif isinstance(element, dict):
            for value in element.values():
                total += process_element(value)
        return total

    total_sum = 0
    for data in args:
        total_sum += process_element(data)
    return total_sum

data_structure1 = [1, 2, 3]
data_structure2 = {'a': 4, 'b': 5}
data_structure3 = (6, {'cube': 7, 'drum': 8})
data_structure4 = "Hello"
data_structure5 = ((), [{(2, 'Urban', ('Urban2', 35))}])
data_structure6 = 58

result = calculate_structure_sum(
    data_structure1,
    data_structure2,
    data_structure3,
    data_structure4,
    data_structure5,
    data_structure6
)
print(result)


