# computing a list of max from a key/value input
# input :
#     * a filename to a file with the list of couple of letter(key) and an integer (value) as (a,3) separate by ';' # output
#     * n number of max to return
# ouput :
#     the list key of the keys of the n max value as python list [a,f,3]
# the resolution must be done in less time than the naive implemented here on big files tests
# ____________
# command : max
# args :
#   - pathfile
#   - n
# n must be changed to 1 of negative or null
# the naive algorithm implemeted
# run is the function called by the test runner


def max_in_list(s):
    pairs = s.replace("(", "").replace(")", "").split(";")
    l = [pair.split(",") for pair in pairs]
    k = max(l, key=lambda t: int(t[1]))
    return f"{k[0]},{k[1]}"


def get_x_max(path, n):
    nbmax = int(n)
    if nbmax < 1:
        nbmax = 1

    flist = open(path, "r")
    s = flist.read()
    keys = []
    while len(keys) < nbmax:
        max = max_in_list(s)
        keys.append(max.split(",")[0])
        s = s.replace("(" + str(max) + ");", "").replace(";(" + str(max) + ")", "")

    return str(keys)


if __name__ == "__main__":
    print(get_x_max("./xmax_1.txt", 1))
    print(get_x_max("./xmax_2.txt", 30))
    print(get_x_max("./xmax_3.txt", 3))
