def make_executable(path):
    """ Use: Takes a script as input and makes it executable """
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)
