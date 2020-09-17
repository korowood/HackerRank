#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if "PM" in s:
        a = s.split(':')
        a[0] = str(int(a[0]) + 12)
        s = ':'.join(a).replace('PM', '')
        print(s)
    else:
        print(s.replace('AM', ''))
    return s

if __name__ == '__main__':


    s = input()

    result = timeConversion(s)
