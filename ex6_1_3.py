def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))


def escape_string(s):
    """Escapes double-quote, tab & new line from string"""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s

json_data = {
    "name": "Advanced Python Training"
}
print json_encode(json_data)

# Passing the json data to the fucnction to get the desired
# output.
