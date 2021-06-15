import sys

print(sys.version, sys.platform)


def show_size(x, level=0):
    print('t' * level, f"type={x.__class__}, size= {sys.getsizeof(x)}, object= {x}", )
    if hasattr(x, '_iter_'):
        if hasattr(x, 'items'):
            xx: object
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


def my_func(num_list):
    f = open("1.txt", "r")

    a = "tmp"
    b = "1.txt"
    c = "2.txt"
    ENC = "utf-8"
    print("Данные после выполения задачи:")
    with open(b, encoding=ENC) as b, open(c, "w", encoding=ENC) as c:
        for line in b:
            if a not in line:
                c.write(line)
    f = open("2.txt", "r")
    return locals()


show_size(my_func)
