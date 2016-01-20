def unflatten_dict(a):
    """
    do the reverse of flatten_dict
    >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'c': 4, 'b': {'y': 3, 'x': 2}}
    """
    result = {}
    for key in a.keys():
        if "." in key:
            p, c = key.split(".", 1)
            if p in result.keys():
                result[p].update(unflatten_dict({c: a[key]}))
            else:
                result.update({p: unflatten_dict({c: a[key]})})
        else:
            result.update({key: a[key]})
    return result


print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})

# Write a function unflatten_dict to do
# reverse of flatten_dict.
