def directory_setup(prefix,path):
    """ Use: Takes a path and prefix and creates a directory if it doesnt exist """
    for element in prefix:
       dir = path + "/" + element
       if not os.path.isdir(dir):
          os.makedirs(dir)
