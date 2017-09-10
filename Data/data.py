def sanitize(time_string):
    '''This tool removes the dash and colons
    and replaces them for dots. It normalizes the input to mins.secs'''
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def open_files(file_name):
    try:
        with open(file_name) as file:
            data = file.readline()

        return data.strip().split(',')
    except IOError as err:
        print('Error: '+str(err))
        return None


james = open_files('james.txt')
julie = open_files('julie.txt')
mikey = open_files('mikey.txt')
sarah = open_files('sarah.txt')


print(sorted(set([sanitize(each_t) for each_t in james]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in julie]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in mikey]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in sarah]))[0:3])

