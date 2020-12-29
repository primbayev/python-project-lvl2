import json
import yaml


def priorotize_dict(pairs, dict):
    pairs_copy = list(pairs.copy())

    for pair in pairs:
        if pair in dict.items():
            pairs_copy.remove(pair)
            pairs_copy.insert(0, pair)

    return pairs_copy


def get_file_format(file_path):
    if file_path.endswith('.yaml'):
        return 'yaml'
    elif file_path.endswith('.json'):
        return 'json'


def decode_files(file_path1, file_path2):
    first_file_format = get_file_format(file_path1)
    second_file_format = get_file_format(file_path2)

    if first_file_format == 'json':
        dict1 = json.load(open(file_path1))
    elif first_file_format == 'yaml':
        dict1 = yaml.load(open(file_path1), Loader=yaml.Loader)

    if second_file_format == 'json':
        dict2 = json.load(open(file_path2))
    elif second_file_format == 'yaml':
        dict2 = yaml.load(open(file_path2), Loader=yaml.Loader)

    return dict1, dict2


def generate_diff(file_path1, file_path2):
    dict1, dict2 = decode_files(file_path1, file_path2)

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
