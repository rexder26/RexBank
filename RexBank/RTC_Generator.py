import time,os,random
#
odds = []
for num in range(42):
    if num % 2 != 0:
        odds.append(num)
print(odds)
def GEN():
    Choice = [0, 1, 2, 3, 4, 'A', 'B', 'C', 'R', 'E', 'X',odds]
    rand_id = random.randrange(len(Choice))
    rand_id1 = random.randrange(len(Choice))
    rand_id2 = random.randrange(len(Choice))
    rand_id3 = random.randrange(len(Choice))
    access = input("Enter You Account CODE: ")
    acc = ('.\\DB\\Acc\\%s.rtc' % access)
    acc_r = open(acc, "r")
    acc_read = acc_r.read() #It Reads The Text Database That Have The user Name.   #SELECT
#
    def acc_write(write): #It Writes TO The Database.   #INPUT
        acc_w = open(acc, "w")
        acc_w.write(write)
        acc_w.close()
#
    try:
        oo = open(acc)
        random_selection = str(Choice[rand_id]) + str(Choice[rand_id1]) + str(Choice[rand_id2]) + str(Choice[rand_id3] + str(odds[1]))
        print("See the Code Below For 3 Seconds...\n CODE: ", random_selection)
#
        time.sleep(3)
        os.system("cls")
#
        user = input("Enter The Code Here: ")
#
        if user == random_selection:
            print("Good JOB")
            inc = int(acc_read) + 100
            acc_write(str(inc))
            print("CONGRATULATIONS!!!\nYou Have Earned 100RTC.")
            GEN()
        else:
            print("Error!!!")
            os.system("pause")
            GEN()
    except:
        print("Their Is no Account by the Code")
GEN()
def square():
    print("**********")
    print("**********")
    print("**      **")
    print("**      **")
    print("**      **")
    print("**********")
    print("**********")
def __dir__():
    print("Hello World")
square()
