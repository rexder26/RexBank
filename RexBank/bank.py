import time
import sys
import os

# Login
banner = '''
|||||||||||||||||||||||||||||||
WellCome To Rex Bank of rexcoin
|||||||||||||||||||||||||||||||
'''


def Log1():
    print(banner)
    print("1) Login")
    print("2) Sign UP")
    print("00) Cancel")
    first = input(">>")
    if first == "1":
        login = input("Enter Your Code: ")
        file = ('.\\DB\\Users\\%s.rtc' % login)
        try:
            user_r = open(file, "r")
            print("=============================\nWelcome, %s\n=============================" % user_r.read())
            user_r.close()

            def Bank():
                # Configurations TO Read and Write On the Text Database
                acc = ('.\\DB\\Acc\\%s.rtc' % login)
                acc_r = open(acc, "r")
                acc_read = acc_r.read()

                def acc_write(write):
                    acc_w = open(acc, "w")
                    acc_w.write(write)
                    acc_w.close()

                sec = input("What Do you Want to Do? \n 1) Balance\n 2) Withdraw\n 3) Transaction\n 4) Log Out\n 5) "
                            "Close\n >> ")
                if sec == "1":
                    print("===============================================\nYour Current Balance is %sRTC \n "
                          "--------------------------------------" % acc_read)
                    Bank()
                elif sec == "2":
                    withd = input("Enter The Amount of Withdraw: ")
                    try:
                        if int(withd) > int(acc_read):
                            print("You Only Have %sRTC, \n Please EARN "
                                  "more!!!\n---------------------------------------------" % (acc_read))

                            Bank()
                        else:
                            minus = int(acc_read) - int(withd)
                            acc_write(str(minus))
                            print("-------------------------------------------\nYou have Withdrawn %sRTC. \n Your Current Balance is %sRTC\n---------------------------------" % (withd, minus))
                            os.system("cls")
                            Bank()
                    except:
                        print("Please Enter Money Amount Only!!!")
                        os.system("cls")
                        Bank()
                elif sec == "3":
                    rec = input("Enter The User Code That You want To Send RTC: ")
                    rec1 = ('.\\DB\\Users\\%s.rtc' % rec)
                    try:
                        receiver= open(rec1, "r")
                        user_sent = input("Enter the Amount: ")

                        # Configurations TO Read and Write On the Text Database
                        acc_rec = ('.\\DB\\Acc\\%s.rtc' % rec)
                        acc_rec_r = open(acc_rec, "r")
                        acc_rec_read = acc_rec_r.read()

                        def acc_rec_write(write):
                            acc_rec_w = open(acc_rec, "w")
                            acc_rec_w.write(write)
                            acc_rec_w.close()

                        if int(user_sent) > int(acc_read):
                            print("============================================\nYou Only Have %sRTC, \n You can't send This Much Amount.\n=====================================" % acc_read)
                            Log1()
                        else:
                            sent = int(acc_read) - int(user_sent)
                            acc_write(str(sent))

                            # Sending The RTC
                            inc = int(acc_rec_read) + int(user_sent)
                            acc_rec_write(str(inc))
                            print("You  Have Sent %sRTC TO %s Account." % (user_sent, receiver.read()))

                            Bank()
                    except:
                        print("InValid Error!! Try Again...")

                        Bank()
                elif sec == "4":
                    Log1()
                elif sec == "5":
                    user_r.close()
                    acc_r.close()
                    print("RexCOIN Bank Database Closed Successfully!!!")
                    os.system("pause")

            Bank()
        except:
            print("You are new User. Please, SignUp")
            Log1()
    elif first == "2":
        create = input("Enter Your CODE: ")
        name = input("Enter Your Name: ")
        try:
            print("Creating An Account to %s." % name)
            os.system("echo off")
            os.chdir("E:/Projects/Programming/Python/Bank/DB/Users")
            os.system("echo %s>%s.rtc" % (name, create))
            os.chdir("E:/Projects/Programming/Python/Bank/DB/Acc")
            os.system("echo RTC>%s.rtc" % create)
            os.chdir("E:/Projects/Programming/Python/Bank")

            # Config The Database
            acc_rec = ('.\\DB\\Acc\\%s.rtc' % create)
            acc_rec_r = open(acc_rec, "r")
            acc_rec_read = acc_rec_r.read()

            def acc_rec_write(write):
                acc_rec_w = open(acc_rec, "w")
                acc_rec_w.write(write)
                acc_rec_w.close()

            acc_rec_write("0")

            time.sleep(2)
            print("Account Created Successfully!!! \n You need to Reboot The Program For Your Security")
            time.sleep(0.5)
            quit()

        except:
            print("Invalid Name, Try again!!!")
    elif first == "00":
        exit()
    else:
        print("Enter Number [1,2,00]")
        Log1()


Log1()
