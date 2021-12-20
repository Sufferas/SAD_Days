# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def day_2_2(name):
    with open(name) as f:
        contents = f.readlines()


    down = 'down'
    down_num = 0
    up = 'up'
    up_num = 0
    forward = 'forward'
    forward_num = 0

    goal_num= 0
    tiefe_num = 0

    for content in contents:
        content_split = str(content).split(" ")
        if content_split[0] == down:
            down_num = down_num + int(content_split[1])
            goal_num = goal_num + int(content_split[1])
        elif content_split[0] == up:
            up_num = up_num + int(content_split[1])
            goal_num = goal_num - int(content_split[1])
        elif content_split[0] == forward:
            forward_num = forward_num + int(content_split[1])
            tiefe_num = tiefe_num + (goal_num*int(content_split[1]))

    result = tiefe_num * forward_num
    print(result)


def day_2(name):
    # Use a breakpoint in the code line below to debug your script.
    with open(name) as f:
        contents = f.readlines()

    down = 'down'
    down_num = 0
    up = 'up'
    up_num=0
    forward = 'forward'
    forward_num = 0

    for content in contents:
        content_split = str(content).split(" ")
        if content_split[0] == down:
            down_num = down_num + int(content_split[1])
        elif content_split[0] == up:
            up_num = up_num + int(content_split[1])
        elif content_split[0] == forward:
            forward_num = forward_num + int(content_split[1])

    down_up = down_num - up_num
    result = down_up*forward_num
    print(result)


def day_1(name):
    # Use a breakpoint in the code line below to debug your script.
    with open(name) as f:
        contents = f.readlines()
    count = 0
    num = 0
    for content in contents:
        if num < int(content):
            count = count + 1
        num = int(content)
    print(count-1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # day_1('input.txt')
    # day_2('input2.txt')
    day_2_2('input2.txt')
    # day_3('input3.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/