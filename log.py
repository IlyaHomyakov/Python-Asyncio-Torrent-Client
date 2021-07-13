def write(*args):
    log_file = open('log.txt', 'a')
    log_file.write(str(args) + '\n')
