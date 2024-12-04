import sys  # use sys module to get comand line arguments


def main():
    # get command line arguments
    args = sys.argv
    if len(args) < 2:
        print('No files received')
        return
    args = args[1:]
    results = {}
    for file_name in args:
        result = parse_file(file_name)
        results[file_name] = result
    return results
    
def parse_file(file_name):
    with open(file_name) as f:
        data = f.read().strip()
    identifiers = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for identifier in identifiers:
        count = data.count(identifier)
        identifiers[identifier] = count
    identifiers['Unknown'] = len(data) - sum(identifiers.values())
    return identifiers

if __name__ == '__main__':
    main()