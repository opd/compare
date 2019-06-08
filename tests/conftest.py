from compare import BaseCompare


def pytest_assertrepr_compare(op, left, right):
    if (
        isinstance(left, BaseCompare) or isinstance(right, BaseCompare)
    ) and op == "==":
        if isinstance(left, BaseCompare):
            return left.compare_error(right, is_left=True)
        else:
            return right.compare_error(left, is_left=False)
