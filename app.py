from colorama import Fore, Back, Style
from getpass import getpass # hide password module
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleService
import os, sys, time

__user_service=UserService()
__news_service=NewsService()
__role_service=RoleService()

while True:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX, '\n\t==================')
    print(Fore.LIGHTBLUE_EX,'\n\twelcome to news system')
    print(Fore.LIGHTBLUE_EX, '\n\t==================')
    print(Fore.LIGHTGREEN_EX,'\n\t1.login')
    print(Fore.LIGHTGREEN_EX,'\n\t2.exit')
    print(Style.RESET_ALL)

    opt=input('\n\tPlease type option code here: ')
    if opt=='1':
        username=input('\n\tPlease type your username: ')
        password=getpass('\n\tPlease type your password: ')
        result = __user_service.login(username, password)
        if result == True:
            # search user role(admin or normal user)
            role=__user_service.search_user_role(username)
            os.system('cls')
            while True:
                os.system('cls')
                if role=='news_editor':
                    print(Fore.LIGHTRED_EX, '\n\teditor module is still not release!')
                elif role=='admin':
                    print(Fore.LIGHTGREEN_EX,'\n\t1.edit news report')
                    print(Fore.LIGHTGREEN_EX, '\n\t2.manage user')
                    print(Fore.LIGHTRED_EX, '\n\tback')
                    print(Fore.LIGHTRED_EX, '\n\texit')
                    print(Style.RESET_ALL)
                    opt = input('\n\tPlease type option code here: ')
                    if opt=='1':
                        while True:
                            os.system('cls')
                            print(Fore.LIGHTGREEN_EX, '\n\t1.review news report')
                            print(Fore.LIGHTGREEN_EX, '\n\t2.delete news report')
                            print(Fore.LIGHTRED_EX, '\n\tback---to prev step')
                            print(Style.RESET_ALL)
                            opt=input('\n\tPlease type option code here: ')
                            if opt == '1':
                                page = 1
                                while True:
                                    os.system('cls')
                                    count_page = __news_service.search_unreview_count_page()
                                    result = __news_service.search_unreview_list(page)
                                    for i in range(len(result)):
                                        news = result[i]
                                        print(Fore.LIGHTBLUE_EX, '\n\t{0}\t{1}\t{2}\t{3}'.format(i+1,news[1], news[2], news[3]))
                                    print(Fore.LIGHTBLUE_EX, '\n\t==================')
                                    print(Fore.LIGHTBLUE_EX, '\n\t{0}/{1}'.format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, '\n\t==================')
                                    print(Fore.LIGHTRED_EX, '\n\tback---to prev step')
                                    print(Fore.LIGHTRED_EX, '\n\tprev---go prev page')
                                    print(Fore.LIGHTRED_EX, '\n\tnext---go next page')
                                    print(Style.RESET_ALL)
                                    opt=input('\n\tPlease type option code here: ')
                                    if opt=='back':
                                        break
                                    elif opt=='prev' and page >1:
                                        page=page-1
                                    elif opt=='next' and page < count_page:
                                        page=page+1
                                    elif 1<=int(opt)<=10:
                                        news_id = result[int(opt)-1][0]
                                        __news_service.update_unreview_news(news_id)

                            elif opt == '2':  # delete news report
                                page = 1
                                while True:
                                    os.system('cls')
                                    count_page = __news_service.search_count_page()
                                    result = __news_service.search_list(page)
                                    for i in range(len(result)):
                                        news = result[i]
                                        print(Fore.LIGHTBLUE_EX, '\n\t{0}\t{1}\t{2}\t{3}'.format(i+1,news[1], news[2], news[3]))
                                    print(Fore.LIGHTBLUE_EX, '\n\t==================')
                                    print(Fore.LIGHTBLUE_EX, '\n\t{0}/{1}'.format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, '\n\t==================')
                                    print(Fore.LIGHTRED_EX, '\n\tback---to prev step')
                                    print(Fore.LIGHTRED_EX, '\n\tprev---go prev page')
                                    print(Fore.LIGHTRED_EX, '\n\tnext---go next page')
                                    print(Style.RESET_ALL)
                                    opt=input('\n\tPlease type option code here: ')
                                    if opt=='back':
                                        break
                                    elif opt=='prev' and page >1:
                                        page=page-1
                                    elif opt=='next' and page < count_page:
                                        page=page+1
                                    elif 1<=int(opt)<=10:
                                        news_id = result[int(opt)-1][0]
                                        __news_service.delete_by_id(news_id)

                            elif opt == 'back':
                                break

                    elif opt == '2':
                        while True:
                            os.system('cls')
                            print(Fore.LIGHTGREEN_EX, '\n\t1.add user')
                            print(Fore.LIGHTGREEN_EX, '\n\t2.update user')
                            print(Fore.LIGHTGREEN_EX, '\n\t3.delete user')
                            print(Fore.LIGHTRED_EX, '\n\tback---to prev step')
                            print(Style.RESET_ALL)
                            opt=input('\n\tPlease type option code here: ')
                            if opt == 'back':
                                break
                            elif opt == '1':
                                os.system('cls')
                                username = input('\n\tusername: ')
                                password = getpass('\n\tpassword: ')
                                re_password = getpass('\n\ttype in your password again: ')
                                if password != re_password:
                                    print('password should be same! return to prev step in 3 sec')
                                    time.sleep(3)
                                    continue
                                email = input('\n\temail: ')
                                result = __role_service.search_list()
                                for i in range(len(result)):
                                    role = result[i]
                                    print(Fore.LIGHTBLUE_EX, '\n\t{0}.{1}'.format(i+1, role[1]))
                                print(Style.RESET_ALL)
                                opt=input('\n\twhat is your role: ')
                                role_id = result[int(opt)-1][0]
                                __user_service.add_user(username, password, email, role_id)
                                print('\n\tsuccessfully save return to prev step in 3 sec')
                                time.sleep(3)

                            elif opt =='2':
                                page = 1
                                while True:
                                    os.system('cls')
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_user_list(page)
                                    for i in range(len(result)):
                                        news = result[i]
                                        print(Fore.LIGHTBLUE_EX,
                                              '\n\t{0}\t{1}\t{2}'.format(i + 1, news[1], news[2]))
                                    print(Fore.LIGHTBLUE_EX, '\n\t==================')
                                    print(Fore.LIGHTBLUE_EX, '\n\t{0}/{1}'.format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, '\n\t==================')
                                    print(Fore.LIGHTRED_EX, '\n\tback---to prev step')
                                    print(Fore.LIGHTRED_EX, '\n\tprev---go prev page')
                                    print(Fore.LIGHTRED_EX, '\n\tnext---go next page')
                                    print(Style.RESET_ALL)
                                    opt = input('\n\tPlease type option code here: ')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page = page - 1
                                    elif opt == 'next' and page < count_page:
                                        page = page + 1
                                    elif 1 <= int(opt) <= 10:
                                        os.system('cls')
                                        user_id = result[int(opt)-1][0]
                                        username = input('\n\tPlease type in your new username: ')
                                        password = getpass('\n\tPlease type in your new username: ')
                                        re_password = getpass('\n\tPlease type in your new username again: ')
                                        if password != re_password:
                                            print(Fore.LIGHTRED_EX, '\n\tpassword should be same! return to prev step in 3 sec')
                                            print(Style.RESET_ALL)
                                            time.sleep(3)
                                            break
                                        email = input('\n\temail: ')
                                        result = __role_service.search_list()
                                        for i in range(len(result)):
                                            role = result[i]
                                            print(Fore.LIGHTBLUE_EX, '\n\t{0}.{1}'.format(i + 1, role[1]))
                                        print(Style.RESET_ALL)
                                        opt = input('\n\twhat is your role: ')
                                        role_id = result[int(opt) - 1][0]
                                        opt = input('\n\tsave it or not? (Y/N)')
                                        if opt == 'Y' or opt == 'y':
                                            __user_service.update_user(user_id, username, password, email, role_id)
                                            print('\n\tsuccessfully save return to prev step in 3 sec')
                                            time.sleep(3)

                                        elif opt == 'N' or opt == 'n':
                                            break

                            elif opt =='3':
                                page = 1
                                while True:
                                    os.system('cls')
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_user_list(page)
                                    for i in range(len(result)):
                                        news = result[i]
                                        print(Fore.LIGHTBLUE_EX,
                                              '\n\t{0}\t{1}\t{2}'.format(i + 1, news[1], news[2]))
                                    print(Fore.LIGHTBLUE_EX, '\n\t==================')
                                    print(Fore.LIGHTBLUE_EX, '\n\t{0}/{1}'.format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, '\n\t==================')
                                    print(Fore.LIGHTRED_EX, '\n\tback---to prev step')
                                    print(Fore.LIGHTRED_EX, '\n\tprev---go prev page')
                                    print(Fore.LIGHTRED_EX, '\n\tnext---go next page')
                                    print(Style.RESET_ALL)
                                    opt = input('\n\tPlease type option code here: ')
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page = page - 1
                                    elif opt == 'next' and page < count_page:
                                        page = page + 1
                                    elif 1 <= int(opt) <= 10:
                                        os.system('cls')
                                        user_id = result[int(opt)-1][0]
                                        opt = input('\n\tsave it or not? (Y/N)')
                                        if opt == 'Y' or opt == 'y':
                                            __user_service.delete_by_id(user_id)
                                            print('\n\tsuccessfully delete return to prev step in 3 sec')
                                            time.sleep(3)
                                        elif opt == 'N' or opt == 'n':
                                            break



                    elif opt=='back':
                        break
                    elif opt=='exit':
                        sys.exit(0)

        else:
            print('\n\tUsername or password incorrect!!! system will return prev page after 3 sec')
            time.sleep(3)

    elif opt=='2':
        sys.exit(0)