def parse_constants_file(filename):
    constants = {}

    with open(filename, 'r') as f:
        lines = f.readlines()
    data_lines = lines[3:]

    for line in data_lines:
        if not line.strip():
            continue  # skip empty lines
        name = line[:25].strip()
        value_str = line[25:45].strip()
        dimension = line[45:].strip()
        try:
            value = float(value_str)
        except ValueError:
            continue  # skip lines with invalid float values
        constants[name] = {'value': value, 'dimension': dimension}
    return constants

if __name__ == '__main__':
    constants = parse_constants_file('constants.txt')
    for name, info in constants.items():
        print(f"{name:25} = {info['value']:>15}  [{info['dimension']}]")