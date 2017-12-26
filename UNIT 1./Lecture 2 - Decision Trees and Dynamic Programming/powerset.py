def powerset1(items):
    powerset = [[]]
    for i in items[1:]:
        subset = [subset + [i] for subset in powerset]
        powerset.extend(subset)
    return powerset

def powerset2(items):
    if items == []:
        yield []
    else:
        for i in powerset2(items[1:]):
            yield i + [items[0]]
            yield i
