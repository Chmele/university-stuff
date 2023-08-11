import functools


def recursion_level(func):
    def wrapper(*args ,**kwargs):
        try:
            func.depth += 1
            ret = func(*args, **{**kwargs, "depth": func.depth})
            func.depth -= 1
        except TypeError:
            raise AssertionError("Need '**kwargs' in method signature declaration")
        return ret
    func.depth = 0
    return wrapper


def flatten(d):
    try: 
        return {
            (k, *kinner): vinner
            for k, v in d.items() 
                for kinner, vinner in flatten(v).items()
        } 
    except AttributeError:
        return {(): d}


def traverse_dict_path(d, path):
    return functools.reduce(lambda cd, s: cd.__getitem__(s), path, d)


def per_itempair(i1, i2, element_mapping=lambda a,b: (a,b), element_filter=lambda a,b: a!=b, **kwargs):
    match i1, i2:
        case dict(), dict(): return dictsum(i1, i2)
        case list(), list(): return listsum(i1, i2)
        case _: return element_mapping(i1, i2) if element_filter(i1, i2) else None
    

def dictsum(d1, d2, per_itempair=per_itempair):
    return {
        k: value
        for k in set((*d1.keys(), *d2.keys()))
        if (value := per_itempair(d1.get(k), d2.get(k)))
    }


def listsum(l1, l2, per_itempair=per_itempair):
    return {
        i: value
        for i, items in enumerate(zip(l1,l2))
        if (value := per_itempair(*items))
    }


def deep_traverse(o, path):
    try:
        p, *rest = path
    except ValueError:
        return o
    if isinstance (p, tuple|list|set):
        return type(p)(iter_traverse(o, path))
    return deep_traverse(o[p], rest)

def iter_traverse(o, path):
    next_path, *rest = path
    return [
        deep_traverse(o, (index, *rest)) 
        for index in next_path or range(len(o))
    ]

def deep_compare(o1, o2, path):
    o1, o2 = (deep_traverse(o, path) for o in (o1, o2))
    return [(i1, i2) for i1, i2 in zip(o1,o2)if i1!=i2]
