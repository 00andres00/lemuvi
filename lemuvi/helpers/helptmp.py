def hwrite(f, m, d):
    with open(f, m) as f:
        f.write(d)

def hread(f):
    with open(f, 'r') as f:
        file = f.read()
    return file

