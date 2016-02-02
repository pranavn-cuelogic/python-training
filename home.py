import getpass
import imaplib
import re
from email.parser import Parser
from email.utils import parseaddr
from validate_email import validate_email


def home():
    print "\n>>>Welcome to Email Accessing System. We will tell you the most top 10 users in your inbox & sent items<<<\n"
    enterEmail()


def enterEmail():
    username = raw_input("Email address: ")
    if validate_email(username):
        password = getpass.getpass()
    else:
        print "Please enter valid email address."
        enterEmail()

    if username != '' and password != '':
        loginAndFetchRawData(username, password)


def loginAndFetchRawData(username, password):
    mail_list = imaplib.IMAP4_SSL("imap.gmail.com")
    mail_list.login(username, password)
    mail_list.list()
    select_option = int(raw_input("\nPlease enter 1 for Inbox OR 2 for Sent Mail: "))
    if select_option == 1:
        folder = 'Inbox'
    elif select_option == 2:
        folder = '[Gmail]/Sent Mail'
    else:
        print "Invalid selection please select proper option"
        loginAndFetchRawData(username, password)

    mail_list.select(folder)
    
    print "Now enter the start date & end date between which you want to fetch emails."
    from_date = raw_input('Enter start date. e.g: 01-Jan-2016: ')
    to_date = raw_input('Enter end date. e.g: 31-Jan-2016: ')
    print "\nProcessing.... it take litte time to process."
    # from_date = "01-Jan-2016"
    # to_date = "01-Feb-2016"
    mail_type, data = mail_list.uid('search', None, '(SENTSINCE {from_date} SENTBEFORE {to_date})'.format(from_date=from_date, to_date=to_date))

    total_email_count = len(data[0].split())

    mail_data = []
    for numid in data[0].split()[::-1]:
        mail_type, data = mail_list.uid('fetch', numid, '(RFC822)')
        for msg_data in data[0]:
            headers = Parser().parsestr(msg_data)
            mail_data.append(headers)

    # print "Total email Count: ", total_email_count
    target = open('emails.txt', 'a')
    target.write(str(mail_data))
    processRawData(total_email_count, mail_data, folder)
    mail_list.close()
    mail_list.logout()


def processRawData(total_email_count, user_data, folder):
    individual_email_count = {}
    for data in user_data:
        if folder == "Inbox":
            user_detail = data['from']
        else:
            user_detail = data['to']
        
        # name = ''
        # if user_detail[0] != '':
        #     name = ''.join(n for n in user_detail[0] if n.isalnum())

        # email = ''
        # if user_detail[1] != '':
        #     email = user_detail[1]

        # print "Name==>", name
        # print "Email==>", email
        # print "Date==>", data['date']
        # print "===xx===xx===xx===\n"

        if user_detail in individual_email_count:
            individual_email_count[user_detail] = individual_email_count[user_detail] + 1
        else:
            individual_email_count[user_detail] = 1
    
    displayResult(individual_email_count, total_email_count)


def displayResult(individual_email_count, total_email_count):
    i = 1
    print '==' * 40
    print "Total no. of emails: ", total_email_count
    print "==>Name<== \t\t\t==>Email<== \t\t\t==>No of emails (in percentage)<=="
    for name, count in sorted(individual_email_count.items(), key=lambda (k,v): (v,k)) :
        if i <= 10:
            percentage = count / float(total_email_count) * 100
            user_detail = parseaddr(name)
            if user_detail[0] != '':
                print "%s\t\t %s\t\t %s" % (user_detail[0], user_detail[1], round(percentage,2))
        
        i += 1
    print '==' * 40
home()

