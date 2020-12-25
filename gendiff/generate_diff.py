import json


def priorotize_dict(pairs, dict):
    pairs_copy = list(pairs.copy())

    for pair in pairs:
        if pair in dict.items():
            pairs_copy.remove(pair)
            pairs_copy.insert(0, pair)

    return pairs_copy


def generate_diff(file_path1, file_path2):
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))

    identical = dict1.items() & dict2.items()
    missed = dict1.items() - dict2.items()
    extra = dict2.items() - dict1.items()

    all_pairs = identical | missed | extra
    all_pairs = priorotize_dict(all_pairs, dict1)

    sorted_pairs = sorted(
        all_pairs, key=lambda pair: pair[0].lower()
    )

    diff = []
    for k, v in sorted_pairs:
        if (k, v) in missed:
            diff.append(('- ' + k, v))
        elif (k, v) in extra:
            diff.append(('+ ' + k, v))
        else:
            diff.append(('  ' + k, v))

    diff = json.dumps(dict(diff), indent=2, separators=('', ': '))

    return diff.replace('\"', '')
