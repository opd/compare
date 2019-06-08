import re


class BaseCompare:
    def compare_error(self, other, is_left=None):
        return [
            self.get_error_first_line(other, is_left),
            'Not implemented',
        ]

    def get_error_first_line(self, other, is_left):
        left, right = other, self._obj
        if is_left:
            left, right = right, left
        return "assert %s == %s" % (left, right)


class Any(BaseCompare):
    def __init__(self, type=None):
        self._type = type

    def __eq__(self, other):
        if self._type:
            try:
                types = iter(self._type)
            except TypeError:
                types = [self._type]
            for _type in types:
                if not isinstance(other, _type):
                    return False
        return True


class List(BaseCompare):
    def __init__(self, arr, cmp_key=None):
        self._cmp_key = cmp_key
        self._obj = arr

    def __eq__(self, other):
        if self._cmp_key:
            other = sorted(other, key=self._cmp_key)
            arr = sorted(self._obj, key=self._cmp_key)
            return other == arr
        return False


class String(BaseCompare):
    def __init__(self, regexp=None):
        self._regexp = regexp

    def __eq__(self, other):
        if self._regexp:
            return bool(re.match(self._regexp, other))
        return False


class Dict(BaseCompare):
    def __init__(self, d):
        self._obj = d

    def __eq__(self, other):
        dict_part = {
            key: other[key] for key in self._obj.keys()
        }
        return dict_part == self._obj
