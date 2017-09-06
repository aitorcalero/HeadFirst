DATAPATH = r'/Users/aitorcalero/Downloads/' \
           r'0636920003434-master-1416388d72726c5f852316e085111af06da60249' \
           r'/code/chapter3/sketch.txt'

try:
    data = open(DATAPATH)

    for eachline in data:
        try:
            (role,line_spoken) = eachline.split(":",maxsplit=1)
            print(role,end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('the datafile is missing or something wrong has happened ')
