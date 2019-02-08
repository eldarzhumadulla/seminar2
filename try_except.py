def try_except(x):
    n = 5
    try:
        n.append(x)
    except AttributeError:
        return "n is not a list"

if __name__ == "__main__":
    print(try_except(1))

