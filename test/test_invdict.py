from collections.abc import Iterable, MutableMapping, Mapping

from jcollections import InvDict


def basic_usage_example():
    fn = InvDict({1: "a", 2: "b", 3: "c"})
    print(fn)
    print(fn.inv)

    assert fn[1] == "a"
    assert fn.inv["a"] == 1

    fn.inv["d"] = 4
    assert fn[4] == "d"
    assert fn.inv["d"] == 4

    print(fn)
    print(fn.inv)

    # fn[4] = "a" # ValueError
    # InvertibleDict({1: "a", 2: "a"}) # ValueError
    # fn = InvertibleDict({1: []}) # TypeError, need hashable values


def delete_min_key(d: MutableMapping) -> None:
    if not d:
        return
    key = min(d)
    del d[key]


def delete_min_example():
    fn = InvDict({1: "a", 2: "b", 3: "c"})
    print(fn)

    delete_min_key(fn)
    print(fn)

    delete_min_key(fn.inv)
    print(fn)


def isinstance_example():
    fn = InvDict({1: "a", 2: "b", 3: "c"})
    assert isinstance(fn, MutableMapping)
    assert issubclass(InvDict, MutableMapping)

    assert isinstance(FakeMutableMapping(), MutableMapping)
    assert issubclass(FakeMutableMapping, MutableMapping)


def deep_min(d):
    if isinstance(d, Mapping):
        return min(deep_min(v) for v in d.values())
    elif isinstance(d, Iterable):
        return min(deep_min(v) for v in d)
    else:
        return d


class MyMapping:
    ...


Mapping.register(MyMapping)


def deep_min_example():
    fn = InvDict({
        "a": frozenset({1, 2, 3}),
        "b": frozenset({4, 5, 6}),
        "c": frozenset({7, 8, 9})
    })
    print(deep_min(fn))
    assert deep_min(fn) == 1


def main():
    basic_usage_example()
    isinstance_example()
    delete_min_example()
    deep_min_example()


if __name__ == '__main__':
    main()
