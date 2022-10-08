import os


def string_creator(indentation, all_paths, last=0):
    line = ""
    for index, elem in enumerate(all_paths):
        if elem == 1 and (index + 1) != indentation:
            line += chr(9474) + "   "  # │
            # print("Index: ", index,"Elem: ", elem, "Last: ", last)
        if (index + 1) == indentation:
            if last == 0:
                line += chr(9500) + chr(9472)  # ├
            if last == 1:
                line += chr(9492) + chr(9472)  # └
            break
        if elem == 0:
            line += "    "
            # print("Index: ", index,"Elem: ", elem, "Last: ", last)

    return line


def print_directory(path, indentation=0, all_paths=[]):
    with os.scandir(path) as it:
        it = sorted(it, key=lambda f: f.name.lower())
        last = len(it) - 1
        indentation += 1
    if indentation > len(all_paths):
        all_paths.append(1)
    else:
        all_paths[indentation - 1] = 1

    for index, entry in enumerate(it):
        if index == last:
            all_paths[indentation - 1] = 0
            print(string_creator(indentation, all_paths, last=1), entry.name)
            if entry.is_dir():
                print_directory(entry.path, indentation)

        else:
            print(string_creator(indentation, all_paths, last=0), entry.name)
            if entry.is_dir():
                print_directory(entry.path, indentation)


if __name__ == '__main__':
    print_directory(".")