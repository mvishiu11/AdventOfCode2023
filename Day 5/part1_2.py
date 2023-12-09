def read_file(file_path):
    """
    Read the contents of the file and return the stripped data.
    """
    with open(file_path) as file:
        data = file.read().strip()
    return data

class Transformer:
    def __init__(self, content):
        """
        Initialize the transformer with the content.
        """
        lines = content.split('\n')[1:]  # Skip the name line
        self.tuples = [tuple(map(int, line.split())) for line in lines]

    def apply_single(self, x):
        """
        Apply a single transformation to the input value.
        """
        for dest, src, sz in self.tuples:
            if src <= x < src + sz:
                return x + dest - src
        return x

    def apply_range(self, ranges):
        """
        Apply transformations to a list of ranges.
        """
        result = []
        for dest, src, sz in self.tuples:
            src_end = src + sz
            new_ranges = []
            while ranges:
                st, ed = ranges.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    new_ranges.append(before)
                if inter[1] > inter[0]:
                    result.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    new_ranges.append(after)
            ranges = new_ranges
        return result + ranges

if __name__ == "__main__":
    input_data = read_file("input.txt")
    test_data = read_file("test.txt")

    parts = input_data.split('\n\n')
    test_parts = test_data.split('\n\n')
    seed, *others = parts
    test_seed, *test_others = test_parts

    seed = [int(x) for x in seed.split(':')[1].split()]
    test_seed = [int(x) for x in test_seed.split(':')[1].split()]
    
    transformers = [Transformer(content) for content in others]
    test_transformers = [Transformer(content) for content in test_others]

    # Test Case 1
    test_results = []
    for x in test_seed:
        for transformer in test_transformers:
            x = transformer.apply_single(x)
        test_results.append(x)
    assert min(test_results) == 35

    # Part 1
    part1_results = []
    for x in seed:
        for transformer in transformers:
            x = transformer.apply_single(x)
        part1_results.append(x)
    print(min(part1_results))

    # Test Case 2
    test_results2 = []
    pairs = list(zip(test_seed[::2], test_seed[1::2]))
    for st, sz in pairs:
        ranges = [(st, st + sz)]
        for transformer in test_transformers:
            ranges = transformer.apply_range(ranges)
        test_results2.append(min(ranges)[0])
    assert min(test_results2) == 46

    # Part 2
    part2_results = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for st, sz in pairs:
        ranges = [(st, st + sz)]
        for transformer in transformers:
            ranges = transformer.apply_range(ranges)
        part2_results.append(min(ranges)[0])
    print(min(part2_results))
