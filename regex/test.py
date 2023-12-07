import re


# all line created on the 15th of the 10th month
def exercise1():
    print("all line created on the 15th of the 10th month: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r'^10-15')
        count = 0
        for line in file:
            match = pattern.match(line)
            if match:
                count += 1
        print(count)



# all line created on the 15th of the 10th month at 10 o'clock 18 min 51 sec
def exercise2():
    print("all line created on the 15th of the 10th month at 10 o'clock 18 min 51 sec: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r'^10-15 10:18:51')
        count = 0
        for line in file:
            match = pattern.match(line)
            if match:
                count += 1
        print(count)


# all line created at 51 sec
def exercise3():
    print("all line created at 51 sec: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r'^\d{2}-\d{2} \d{2}:\d{2}:51')
        count = 0
        for line in file:
            match = pattern.match(line)
            if match:
                count += 1
        print(count)


# all line with lowmemorykiller tags
def exercise4():
    print("all line with lowmemorykiller tags: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r'lowmemorykiller')
        count = 0
        for line in file:
            match = pattern.search(line)
            if match:
                count += 1
        print(count)


# all lines created at 10:18:51 with pid 221
def exercise5():
    print("all lines created at 10:18:51 with pid 221: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r'^\d{2}-\d{2}\s*10:18:51\.\d{3}\s*221')
        count = 0
        for line in file:
            match = pattern.search(line)
            if match:
                count += 1
        print(count)


# all lines that contain an error (E)
def exercise6():
    print("all lines that contain an error (E): ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r' E ')
        count = 0
        for line in file:
            match = pattern.search(line)
            if match:
                count += 1
        print(count)


# all warnings (W) from PackageManager
def exercise7():
    print("all warnings (W) from PackageManager: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r' W PackageManager')
        count = 0
        for line in file:
            match = pattern.search(line)
            if match:
                count += 1
        print(count)


# all ExoPlayer Debug (D) information
def exercise8():
    print("all ExoPlayer Debug (D) information: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern1 = re.compile(r' D ')
        pattern2 = re.compile(r'ExoPlayer')
        count = 0
        for line in file:
            match = pattern1.search(line)
            match2 = pattern2.search(line)
            if match and match2:
                count += 1
        print(count)


# all lines java file errors and warnings (EW .java)
def exercise9():
    print("all lines java file errors and warnings: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern1 = re.compile(r' E ')
        pattern2 = re.compile(r' W ')
        pattern3 = re.compile(r'\.java:')
        count = 0
        for line in file:
            match1 = pattern1.search(line)
            match2 = pattern2.search(line)
            match3 = pattern3.search(line)
            if (match1 or match2) and match3:
                # print(line)
                count += 1
        print(count)


# all lines with the word Thread in the message part
def exercise10():
    print("all lines with the word Thread in the message part: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r':.*?:.*?:.*Thread.*')
        count = 0
        for line in file:
            match = pattern.search(line)
            if match:
                # print(line)
                count += 1
        print(count)


# every source of error
def exercise1_1():
    print("every source of error: ", end="")
    files = []
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r".*([E]).*at.*\(((\w+(\.\w+)):\d+)\)")
        for line in file:
            match = pattern.search(line)
            if match:
                print(match.group(3))
                # files.append(match.group(3))

    # print(files)
# def exercise1_1():
#     print("every source of error: ", end="")
#     with open("android_logcat.log", "r", encoding='utf-8') as file:
#         pattern = re.compile(r".*([E]).*at.*\(((\w+(\.\w+)?):\d+)\)")
#         files = list(map(lambda match: match.group(3), filter(lambda match: match, map(pattern.search, file))))
#
#     print(files)


# all pids
def exercise1_2():
    print("all pids: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r"(([0-9-]+ [0-9:.]+) +([0-9]+) +([0-9]+) ([IDVEFAW]) ([^:]+): (.*))")
        pids = set()
        for line in file:
            match = pattern.search(line)
            if not match:
                continue
            pids.add(match.group(3))
        print(pids)


# pid with the most errors
def exercise1_3():
    print("pid with the most errors: ", end="")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r"(([0-9-]+ [0-9:.]+) +([0-9]+) +([0-9]+) (E) ([^:]+): (.*))")
        pids = {}
        for line in file:
            match = pattern.search(line)
            if not match: continue
            if match.group(3) not in pids:
                pids[match.group(3)] = 1
                continue
            pids[match.group(3)] += 1

        print(max(pids, key=pids.get))


# errors on the main thread
def exercise1_4():
    print("errors on the main thread: ")
    with open("android_logcat.log", "r", encoding='utf-8') as file:
        pattern = re.compile(r"(([0-9-]+ [0-9:.]+) +([0-9]+) +([0-9]+) (E) ([^:]+): (.*))")
        for line in file:
            match = pattern.search(line)
            if not match:
                continue
            if match.group(4) == match.group(3):
                print(line)


def main():
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    # exercise5()
    # exercise6()
    # exercise7()
    # exercise8()
    # exercise9()
    # exercise10()
    #
    # exercise1_1()
    # exercise1_2()
    # exercise1_3()
    exercise1_4()


if __name__ == '__main__':
    main()
