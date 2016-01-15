def new(num_buckets=256):
    """Initializes a Map with given number of buckets."""
    amap = []
    for i in range(0, num_buckets):
        amap.append([])
    return amap


def hash_key(amap, key):
    """Given a key this will create a number and then convert
    it to an index for the amps's buckets."""
    return hash(key) % len(amap)


def get_bucket(amap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(amap, key)
    return amap[bucket_id]


def get_slot(amap, key, default=None):
    """
    Returns the index, key and value of a slot found in a bucket
    Returns -1, key and default (None if not set) when not found.
    """
    bucket = get_bucket(amap, key)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v
    return -1, key, default


def get(amap, key, default=None):
    """Gets the value in a bucket for the given key, or the
    default."""
    i, k, v = get_slot(amap, key, default=default)
    return v


def set(amap, key, value):
    """Sets the key to the value, replacing any existing
    value."""
    bucket = get_bucket(amap, key)
    i, k, v = get_slot(amap, key)

    if i >= 0:
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))


def delete(amap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(amap, key)

    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break


def list(amap):
    """Prints out what's in the Map."""
    for bucket in amap:
        if bucket:
            for k, v in bucket:
                print k, v
