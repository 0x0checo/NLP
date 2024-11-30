import sys

def get_lines(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return lines

def get_durations(lines):
    id_durations = {}

    for line in lines[1:]:
        words = line.split(';')
        word = words[5]
        duration = int(words[1])/1000
        if word:
            if word in id_durations:
                id_durations[word] += duration
            else:
                id_durations[word] = duration
    return id_durations

def main():
    lines = get_lines(sys.argv[1])
    duration = get_durations(lines)
    print(duration)

if __name__=="__main__":
    main()
