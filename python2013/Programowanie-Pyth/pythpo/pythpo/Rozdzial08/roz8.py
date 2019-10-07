
def print_line_lengths(path):
    input = file(path)
    for line in input.readlines():
        print len(line)


# Ta wersja obs³uguje b³êdy, które mog¹ siê pojawiæ, gdy
# plik nie istnieje.
def print_line_lengths(path):
    try:
        input_file = file(path)
    except IOError, error:
        print "problem z odczytem '%s': %s" % (path, error)
        input_text = ""
    else:
        input_text = input_file.read()        
    for line in input.readlines():
        print len(line)

def split_fully(path):
    parent_path, name = os.path.split(path)
    if name == "":
        return (parent_path, )
    else:
        return split_fully(parent_path) + (name, )


def print_dir(dir_path):
    for name in os.listdir(dir_path):
        print os.path.join(dir_path, name)


def cmp_extension(path0, path1):
    return cmp(os.path.splitext(path0)[1], os.path.splitext(path1)[1])


def print_dir_by_ext(dir_path):
    for name in sorted(os.listdir(dir_path), cmp_extension):
        print os.path.join(dir_path, name)

def print_tree(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        print full_path
        if os.path.isdir(full_path):
            print_tree(full_path)


def print_dir_info(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        file_size = os.path.getsize(full_path)
        mod_time = time.ctime(os.path.getmtime(full_path))
        print "%-32s: %8d bajtów, zmodyfikowano %s" % (name, file_size, mod_time)


import os
import shutil

def make_version_path(path, version):
    if version == 0:
        # Wersja 0, wiêc brak przyrostka.
        return path
    else:
        # Dodaj przyrostek do starszej wersji.
        return path + "." + str(version)

def rotate(path, version=0):
    # Skonstruuuj wersjê pliku poddawanego rotacji.
    old_path = make_version_path(path, version)
    if not os.path.exists(old_path):
        # Plik nie istnieje, zg³oœ b³¹d.
        raise IOError, "'%s' nie istnieje" % path
    # Utwórz now¹ nazwê dla pliku.
    new_path = make_version_path(path, version + 1)
    # Czy istnieje ju¿ wersja tego pliku?
    if os.path.exists(new_path):
        # Tak, przejdŸ poziom wy¿ej, by i jej zmieniæ nazwê!
        rotate(path, version + 1)
    # Mo¿emy bezpiecznie zmieniæ nazwê aktualnego pliku.
    shutil.move(old_path, new_path)


def rotate_log_file(path):
    if not os.path.exists(path):
        # Pliku brakuje, wiêc go utwórz.
        new_file = file(path, "w")
        # Od razu zamknij plik, by pozosta³ pusty.
        del new_file
    # Dokonaj rotacji.
    rotate(path)


