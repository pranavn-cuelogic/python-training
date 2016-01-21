def flatten_dict(a, result=None, keys=[]):
    """
    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    """

    if result is None:
        result = {}

    for key, values in a.items():
        if isinstance(values, dict):
            flatten_dict(values, result, keys + [key])
        else:
            result['*'.join(keys + [key])] = values

    return result

print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})

# Write a function flatten_dict to flatten a nested dictionary
# by joining the keys with . character.
