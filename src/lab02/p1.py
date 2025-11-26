def mnmx(nums: list[float | int]):
    if not nums:
        print("Value Error")
        return None
    mn = min(nums)
    mx = max(nums)
    return (mn, mx)


def unique_sorted(nums: list[float | int]):
    return list(sorted(set(nums)))


def flatten(mat: list[list | tuple]):
    flattened_list = []
    for row in mat:
        if isinstance(row, (list, tuple)):
            flattened_list.extend(row)
        else:
            raise TypeError(f"Элемент {row} должен быть list or tuple")
    return flattened_list


print(mnmx([43, 54, 5556, 0]))
print(mnmx([]))
print(mnmx([42]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
