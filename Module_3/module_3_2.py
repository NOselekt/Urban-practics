def is_correct(email):
    endings = ['.com', '.net', '.ru']
    if '@' in email:
        if email[-4:] in endings or email[-3:] in endings:
            return True
    return False


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if is_correct(recipient) and is_correct(sender):
        if recipient != sender:
            if sender == 'university.help@gmail.com':
                print('The message was successfully sent from', sender, 'to', recipient + '.\n')
            else:
                print('ATYPICAL SENDER! The message was sent from', sender, 'to', recipient + '.\n')
        else:
            print('You cannot send a message to yourself!\n')
    else:
        print('You cannot send a message from', sender, 'to', recipient + '.', 'One of the emails is incorrect!\n')

message = '1'
while message:
    print('Enter accordingly a message, address of the recipient and address of the sender.\n')
    message = input()
    recipient = input()
    sender = input()
    print('')
    if sender:
        send_email(message, recipient, sender=sender)
    else:
        send_email(message, recipient)
