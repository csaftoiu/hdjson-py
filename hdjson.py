import io
import json


DEFAULT_OBJ_SEPARATOR = '\n-----\n'


def dump(obj, fp, **kwargs):
    """Dump to fp a new hdjson object. Can be called repeatedly to build a full hdjson file."""
    # dump the object
    json.dump(obj, fp, indent=4, **kwargs)
    # and write the separator
    fp.write(DEFAULT_OBJ_SEPARATOR)


def dumps(obj, **kwargs):
    """Dump one hdjson object to a string. Write these continuously to build a full hdjson file"""
    # dump obj with separator after
    return json.dumps(obj, indent=4, **kwargs) + DEFAULT_OBJ_SEPARATOR


def load_iter(fp, **kwargs):
    """Return an iterator iterating all objects in this hdjson-formatted file."""
    buffer = []

    for line in fp:
        if all(c == '-' for c in line.strip()):
            yield json.loads('\n'.join(buffer), **kwargs)
            buffer = []
            continue

        buffer.append(line)

    if buffer:
        yield json.loads('\n'.join(buffer), **kwargs)


def loads_iter(s, **kwargs):
    """Return an iterator iterating all objects in this hdjson-formatted string."""
    return load_iter(io.StringIO(s), **kwargs)


def load(fp, **kwargs):
    """Return list of all the objects in the hdjson file."""
    return list(load_iter(fp, **kwargs))


def loads(s, **kwargs):
    """Return list of all the objects in the hdjson string."""
    return list(loads(s, **kwargs))
