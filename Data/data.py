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


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time(self,new_time):
        self.times.append(new_time)

    def add_times(self,new_list_times):
        self.times.extend(new_list_times)

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])


def open_files(file_name):
    try:
        with open(file_name) as file:
            data = file.readline()

        templ = data.strip().split(',')
        return (AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as err:
        print('Error: ' + str(err))
        return None


james = open_files('james2.txt')
julie = open_files('julie.txt')
mikey = open_files('mikey.txt')
sarah = open_files('sarah.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))

james.append('0.67')
list = ['0.68','0-34']
james.extend(list)

print(james.top3())
