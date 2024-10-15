import imapclient
import pyzmail

# Email Providers and Their IMAP Servers
imap_servers = {
    'Gmail': 'imap.gmail.com',
    'Outlook': 'imap-mail.outlook.com',
    'Yahoo Mail': 'imap.mail.yahoo.com'
}

def login_imap(email, password, imap_server):
    try:
        conn = imapclient.IMAPClient(imap_server, ssl=True)
        conn.login(email, password)
        print("Login Success!!!")
        return conn
    except imapclient.IMAP4.error as e:
        print(f"Login failed: {e}")
        exit()

def select_folder(conn):
    folders = conn.list_folders()
    print(folders)
    folder_name = input("Enter the folder name: ")
    select_info = conn.select_folder(folder_name, readonly=True)
    print(f"{select_info[b'EXISTS']} messages in {folder_name}")
    return folder_name

def search_emails(conn):
    criteria = input("Enter search criteria (e.g., 'ALL', 'BEFORE 01-Jan-2022'): ")
    UIDs = conn.search(criteria)
    print(UIDs)
    return UIDs

def fetch_email(conn, UIDs):
    email_id = int(input("Enter email ID: "))
    raw_message = conn.fetch([email_id], ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(raw_message[email_id][b'BODY[]'])
    print(message.get_subject())
    print(message.get_address('from'))
    print(message.get_address('to'))
    print(message.get_address('bcc'))
    print(message.text_part)
    print(message.html_part == None)
    print(message.text_part.get_payload().decode('UTF-8'))
    print(message.text_part.charset == None)

def delete_email(conn):
    ans = input("Do you want to delete any email? (Y/N): ")
    if ans.lower() == 'y':
        folder_name = input("Enter the folder name: ")
        conn.select_folder(folder_name, readonly=False)
        UIDs = conn.search(['ALL'])
        print(UIDs)
        email_id = input("Enter email ID: ")
        conn.delete_messages([email_id])

def main():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    provider = input("Enter your email provider (Gmail, Outlook, Yahoo Mail): ")
    imap_server = imap_servers[provider]
    
    conn = login_imap(email, password, imap_server)
    folder_name = select_folder(conn)
    UIDs = search_emails(conn)
    fetch_email(conn, UIDs)
    delete_email(conn)
    conn.logout()
    print("Logout Success!!!")

if _name_ == "_main_":
    main()