import sqlite3
import os
import time
import colorama

Cw = colorama.Fore.WHITE
Cb = colorama.Fore.BLACK
Cc = colorama.Fore.CYAN
Cr = colorama.Fore.RED
Cg = colorama.Fore.GREEN




# This Keep Note Just Takes An English Note.

con_Sqlite = sqlite3.connect('keep_noet.db')
Cr = con_Sqlite.cursor()
Cr.execute("CREATE TABLE if not exists keep_noet (title text, note text, lastChange text)")

print(Cc + 'Hello , Keep Your Note Safely')
time.sleep(2)
os.system('cls')



def main():
    print(Cw + '[1] Show All Note')
    print(Cw + '[2] Searsh of Note')
    print(Cw + '[3] Add New Note')
    print(Cw + '[4] Edit Note')
    print(Cw + '[5] Delete Note')
    main_user()
    print('')




def Show_All_Note():
        for row in Cr.execute(f'SELECT * from keep_noet'):
            print('')
            print(Cw + f'[ Title ] : {row[0]}')
            print(Cw + f'[ Note ] : {row[1]}')
            s = str(row[2]).split()
            y = (s[0].replace('time.struct_time(tm_year=', '').replace(',', ''))
            m = (s[1].replace('tm_mon=', '').replace(',', ''))
            d = (s[2].replace('tm_mday=', '').replace(',', ''))
            h = (s[3].replace('tm_hour=', '').replace(',', ''))
            m = (s[4].replace('tm_min=', '').replace(',', ''))
            alldate = f'{y}:{m}:{d}:{h}:{m}'
            print(Cw + f'[ Last Change ] : {alldate}')
            con_Sqlite.commit()
            print('')
        time.sleep(5)
        os.system('cls')
        main()
    



def Searsh_of_Note():
    print('')
    search = input(Cw + '[!] Enter The Title of Note >> ').strip()
    if len(search) > 0: 
        for row in Cr.execute(f'SELECT title, note, lastChange, title from keep_noet Where title = "{search}"'):
            print('')
            print(Cw + f'[ Title ] : {row[0]}')
            print(Cw + f'[ Note ] : {row[1]}')
            s = str(row[2]).split()
            y = (s[0].replace('time.struct_time(tm_year=', '').replace(',', ''))
            m = (s[1].replace('tm_mon=', '').replace(',', ''))
            d = (s[2].replace('tm_mday=', '').replace(',', ''))
            h = (s[3].replace('tm_hour=', '').replace(',', ''))
            m = (s[4].replace('tm_min=', '').replace(',', ''))
            alldate = f'{y}:{m}:{d}:{h}:{m}'
            print(Cw + f'[ Last Change ] : {alldate}')
            con_Sqlite.commit()
            print('')
        time.sleep(5)
        os.system('cls')
        main()




def Add_New_Note():
    print('')
    title = input(Cw + '[ Title ] >> ').strip()
    if len(title) == 0:
        while True:
            if len(title) == 0: title = input(Cr + '[ Please Title ] >> ').strip()
            else: break
    note = input(Cw + '[ Note ] >> ').strip()
    if len(note) == 0:
        while True:
            if len(note) == 0: note = input(Cr + '[ Please Note ] >> ').strip()
            else: break
    Cr.execute(f"insert into keep_noet(title, note, lastChange) values('{title}', '{note}', '{time.localtime()}')")
    for row in Cr.execute(f"SELECT title, note, lastChange, title from keep_noet Where title = '{title}'"):
        print('')
        print(Cw + f'[ Title ] : {row[0]}')
        print(Cw + f'[ Note ] : {row[1]}')
        s = str(row[2]).split()
        y = (s[0].replace('time.struct_time(tm_year=', '').replace(',', ''))
        m = (s[1].replace('tm_mon=', '').replace(',', ''))
        d = (s[2].replace('tm_mday=', '').replace(',', ''))
        h = (s[3].replace('tm_hour=', '').replace(',', ''))
        m = (s[4].replace('tm_min=', '').replace(',', ''))
        alldate = f'{y}:{m}:{d}:{h}:{m}'
        print(Cw + f'[ Last Change ] : {alldate}')
        print('')
        con_Sqlite.commit()
        print('')
    time.sleep(5)
    os.system('cls')
    main()
 



def Edit_Note():
    print('')
    search = input(Cw + '[!] Enter The Title of Note >> ').strip()
    if len(search) > 0: 
        for row in Cr.execute(f'SELECT title, note, lastChange, title from keep_noet Where title = "{search}"'):
            print('')
            print(Cw + f'[ Title ] : {row[0]}')
            print(Cw + f'[ Note ] : {row[1]}')
            s = str(row[2]).split()
            y = (s[0].replace('time.struct_time(tm_year=', '').replace(',', ''))
            m = (s[1].replace('tm_mon=', '').replace(',', ''))
            d = (s[2].replace('tm_mday=', '').replace(',', ''))
            h = (s[3].replace('tm_hour=', '').replace(',', ''))
            m = (s[4].replace('tm_min=', '').replace(',', ''))
            alldate = f'{y}:{m}:{d}:{h}:{m}'
            print(Cw + f'[ Last Change ] : {alldate}')
            print('')
            con_Sqlite.commit()
    print(Cw + '[!] if Input is Empty ( Input = Last Input )')
    user_inputTitle = input(Cw + '[!] Enter Title After Edit >> ').strip()
    user_inputNote = input(Cw + '[!] Enter Title After Edit >> ').strip()
    if len(user_inputTitle) > 0:
        Cr.execute(f'update keep_noet set title = "{user_inputTitle}" where title = "{search}"')
        con_Sqlite.commit()
    elif len(user_inputNote) > 0:
        Cr.execute(f'update keep_noet set note = "{user_inputNote}" where title = "{search}"')
        con_Sqlite.commit()
    Cr.execute(f'update keep_noet set lastChange = "{time.localtime()}" where title = "{search}"')
    con_Sqlite.commit()
    print('')
    if len(user_inputTitle) > 0: 
        for row in Cr.execute(f'SELECT title, note, lastChange, title from keep_noet Where title = "{user_inputTitle}"'):
            print('')
            print(Cw + f'[ Title ] : {row[0]}')
            print(Cw + f'[ Note ] : {row[1]}')
            s = str(row[2]).split()
            y = (s[0].replace('time.struct_time(tm_year=', '').replace(',', ''))
            m = (s[1].replace('tm_mon=', '').replace(',', ''))
            d = (s[2].replace('tm_mday=', '').replace(',', ''))
            h = (s[3].replace('tm_hour=', '').replace(',', ''))
            m = (s[4].replace('tm_min=', '').replace(',', ''))
            alldate = f'{y}:{m}:{d}:{h}:{m}'
            print(Cw + f'[ Last Change ] : {alldate}')
            con_Sqlite.commit()
            print('')
        time.sleep(5)
        os.system('cls')
        main()




def Delete_Note():
        print('')
        search = input(Cw + '[!] Enter The Title You Want To Delete >> ').strip()
        Cr.execute(Cw + f"delete from keep_noet where title = '{search}'")
        print(Cg + '[!] Deleted successfully')
        con_Sqlite.commit()
        print('')
        time.sleep(5)
        os.system('cls')
        main()
        


def main_user():
    user_input = input(Cw + '[!] Enter The Option >> ').strip()
    if user_input in ['1', '2', '3', '4', '5']:
        if user_input == '1':

            Show_All_Note()

        elif user_input == '2':

            Searsh_of_Note()

        elif user_input == '3':

            Add_New_Note()

        elif user_input == '4':

            Edit_Note()

        elif user_input == '5':

            Delete_Note()
        else:
            print(Cr + f'[!] The Option "{user_input}" Not Found')
            print('')
main()