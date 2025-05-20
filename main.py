from colorama import Fore, Style
import os, socket, sys, requests, pywhatkit, pyshorteners, base64, qrcode, sqlite3, platform, time, datetime, random
from faker import Faker  
from prettytable import PrettyTable
from random import sample
import PyPDF2

faker = Faker()  

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
date = datetime.datetime.now()

class color:
    blue = Fore.BLUE + Style.BRIGHT
    red = Fore.RED + Style.BRIGHT
    white = Fore.WHITE + Style.BRIGHT
    reset = Fore.RESET + Style.RESET_ALL

def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def reset_color():
    print(color.reset)

def exit():
    reset_color()
    clear()
    sys.exit()

def ret():
    choice = input(color.white + '[&] Press any key to return to the menu: ')
    main()

def error():
    print(color.white + f'\n[&] Inexpected error in the {color.red}THN-Multitool{color.white}')
    ret()

def get_ip():
    print(color.white + '\n[&] Your IP adress is: ' + color.red + ip)
    ret()

def verify():
    try:
        res = requests.get('https://www.google.com')
        print(color.white + f'\n[&] You are {color.red}connected{color.white} to Internet')
    except:
        print(color.white + f"\n[&] You {color.red}aren't connected{color.white} to Internet")
    ret()

def send_discord():
    try:
        webhook = input(color.white + '\n[&] Enter the URL of your server WebHook: ')
        message = input(color.white + '[&] Enter the message to send: ')
        requests.post(webhook, json={'username': 'BlueWolf', 'content': message})
        print(color.white + f'[&] Message {color.red}sended{color.white} successfully')

    except:
        error()

def gen_ip():
    false_ip = faker.ipv4() 
    print(color.white + '\n[&] The false IP address is: ' + color.red + false_ip)
    ret()

def gen_phone():
    false_phone = faker.phone_number()
    print(color.white + '\n[&] The false phone number is: ' + color.red + false_phone)
    ret()

def send_whatsapp():
    try:
        choice = input(color.white + '\n[&] Enter the phone number to send the message: ')
        message = input(color.white + '[&] Enter the message to send: ')
        pywhatkit.sendwhatmsg_instantly(choice, message)
        
        print(f'\n[&] Message {color.red}sended{color.white} successfully')
        
    except:
        error()

    ret()

def binary():
    choice = input(color.white + '\n[&] Enter the plain text to convert: ')
    binary = ' '.join(format(ord(caracter), '08b') for caracter in choice)
    print(color.white + '[&] The binary code generated is: ' + color.blue + binary)
    ret()

def parrot():
    try:
        os.system('curl parrot.live')

    except KeyboardInterrupt:
        print(color.white + f'\n\n[&] Operation {color.red}interrupted')
    
    except:
        error()

    ret()

def info():
    choice = f'''
[&]: Turkic multitool by {color.red}Masrova
{color.white}[&] Discord server: {color.red}https://discord.gg/BcdSWceD6U
{color.white}[&] Web page: {color.red}https://github.com/Veyk0/Turkic-MULTITOOL.git
'''
    print(color.white + choice)
    ret()

def get_public():
    res = requests.get('https://api.ipify.org?format=json')
    public_ip = res.json()['ip']

    print(color.white + f'\n[&] The public IP adress is: ' + color.red + public_ip)
    ret()

def generate_pass():   
    measure = int(input(color.white + '\n[&] Enter the measure in characters of your password: '))

    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = abc_lower.upper() 
    
    numbers = "0123456789"
    characters = "{}[]()*;/,_-"
    
    sequence = abc_lower + abc_upper + numbers + characters
    password = sample(sequence, measure)
    

    password_result = "".join(password)
    print(color.white + '[&] The result password is: ' + color.red + password_result)
    ret()

def read_pdf():
    choice = input(color.white + '\n[&] Enter the path or the name of the PDF file to read: ')
    reader = PyPDF2.PdfReader(choice)

    print(color.white + '[&] The PDF have ' + color.red + str(len(reader.pages)) + color.white + 'pages')
    print(color.white + '[&] The text of the PDF file is: \n' + color.red + reader.pages[0].extract_text())

    ret()

def mask_url():
    s = pyshorteners.Shortener()
    choice = input(color.white + '\n[&] Enter the URL to mask: ')
    try:
        ey = s.isgd.short(choice)
        mod = input(color.white + '[&] Enter the domain you want to supplant (eg. https://google.com): ')
        word = input(color.white + '[&] Enter the social engineering words separated by "-" (eg. free-gems): ')
        ey = ey.replace("https://", "")
        print(color.white + f'[&] The masked URL: {color.red}{mod}-{word}@{ey}')

    except:
        error()

    ret()

def enc_base64():
    choice = input(color.white + '\n[&] Enter the plain text to encode: ')

    text_bytes = choice.encode('utf-8')
    encrypted_text = base64.b64encode(text_bytes)

    print(color.white + '[&] The text encrypted in base64 is: ' + color.red + str(encrypted_text.decode("utf-8")))
    ret()

def get_size():
    choice = input(color.white + '\n[&] Enter the file or path to the file to view size: ')

    sizefile = os.stat(choice).st_size
    print(color.white + '[&] The size of the file is: ' + color.red + str(sizefile) + color.white + ' bytes')
    ret()

def qr_code():
    try:
        choice = input(color.white + '\n[&] Enter the URL or text to generate in the QR Code: ')
        arch = input(color.white + '[&] Enter the archive name to save the QR Code (the .png is auto completed): ')

        img = qrcode.make(choice)
        f = open(arch + '.png', "wb")
        img.save(f)
        f.close()

        print(color.white + '\n[&] The QR Code is generated in the file ' + color.red + arch)

    except:
        error()

    ret()  

def clear_chrome_history():
    if platform.system() == 'Windows':
        history_path = os.path.expanduser('~') + r'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
    elif platform.system() == 'Linux':
        history_path = os.path.expanduser('~') + '/.config/google-chrome/Default/History'
    else:
        print(color.white + f'[&]: System {color.red}not supported{color.white} for Chrome')
        return
    
    if os.path.exists(history_path):
        conn = sqlite3.connect(history_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM urls")
        conn.commit()

        cursor.close()
        conn.close()

        print(color.white + f'[&] Chrome history {color.red}deleted{color.white} successfully')
    else:
        print(color.white + f"[&] Chrome historial archive " + color.red + 'not found')

def clear_firefox_history():
    if platform.system() == "Windows":
        profiles_path = os.path.expanduser('~') + r"\AppData\Roaming\Mozilla\Firefox\Profiles"
    elif platform.system() == "Linux":
        profiles_path = os.path.expanduser('~') + "/.mozilla/firefox/"
    else:
        print(color.white + f'[&] System {color.blue}not supported{color.white} for Firefox')
        return

    for root, dirs, files in os.walk(profiles_path):
        for dir in dirs:
            profile_path = os.path.join(root, dir)
            places_path = os.path.join(profile_path, "places.sqlite")
            if os.path.exists(places_path):
                conn = sqlite3.connect(places_path)
                cursor = conn.cursor()

                cursor.execute("DELETE FROM moz_historyvisits")
                cursor.execute("DELETE FROM moz_places")
                conn.commit()

                cursor.close()
                conn.close()

                print(color.white + f'[&] Firefox history {color.red}deleted{color.white} successfully')
                return

    print(color.white + f"[&] Firefox historial archive " + color.red + 'not found')

def clear_browser_history():
    browsers = {
        "Chrome": clear_chrome_history,
        "Firefox": clear_firefox_history,
    }

    for browser, clear_func in browsers.items():
        try:
            clear_func()
        except Exception as e:
            error()

def history():
    print(color.white + '\n[&] Cleaning history...')
    try:
        clear_browser_history()
        ret()

    except:
        error()

    ret()

def mp3():
    try:
        print(color.white + '\n[&] The version is only support for ' + color.red + 'Windows')
        choice = input(color.white + '\n[&] Enter the URL of the YouTube video to download mp3: ')
        os.system(f'youtube-download-cli "{choice}" mp3')
        print(color.white + '[&] The audio was saved in the ' + color.red + 'downloads ' + color.white + 'folder')
        
    except:
        error()
        
    ret()

def mp4():
    try:
        print(color.white + '\n[&] The version is only support for ' + color.red + 'Windows')
        choice = input(color.white + '\n[&] Enter the URL of the YouTube video to download mp3: ')
        os.system(f'youtube-download-cli "{choice}" mp3')
        print(color.white + '[&] The video was saved in the ' + color.red + 'downloads ' + color.white + 'folder'),

    except:
        error()
        
    ret()

def table():
    choice = int(input(color.white + '\n[&] Enter the number of people to generate data: ' + color.white))

    table = PrettyTable()
    table.field_names = ["Name", "Last Name", "Email", "Adress", "City", "Phone Number", "IP"]

    for _ in range(choice):
        name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        adress = faker.address()
        city = faker.city()
        phone_number = faker.phone_number()
        ip = faker.ipv4()
        table.add_row([name, last_name, email, adress, city, phone_number, ip])

    print(table)
    ret()

def read():
    try:
        print(color.white + f'\n[&] The database {color.blue}content{color.white} is: \n')
        arch = open('data/xss-sites.txt')
        print(color.blue + arch.read() + '\n')
    except:
        error()

    ret()

def change_theme():
    color.red = Fore.GREEN + Style.BRIGHT
    color.white = Fore.WHITE + Style.BRIGHT

    print(color.white + '\n[&] Color theme changed to green')
    ret()

def scan(target):
    try:
            print(color.white + '\n[&] Starting scanning to ' + color.red + target + color.white + '\n')
            for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                
                result = s.connect_ex((target,port))
                if result ==0:
                    print(color.blue + 'The port {} is open'.format(port))
                s.close()
                
    except KeyboardInterrupt:
        print(color.white + '\n[&] Operation interrupted')
        ret()

    except socket.gaierror:
        print(color.white + '\n[&]Hostname could not be resolved')
        ret()

    except socket.error:
        print(color.white + '\n[&] Server not responding')
        ret()

def scanner():
    target = input(color.white + '\n[&] Enter the target IP to scan: ')
    scan(target)

def system_scanner():
    scan(ip)

def gen_dni():
    POSSIBLE_LETTERS = (
        "T",
        "R",
        "W",
        "A",
        "G",
        "M",
        "Y",
        "F",
        "P",
        "D",
        "X",
        "B",
        "N",
        "J",
        "Z",
        "S",
        "Q",
        "V",
        "H",
        "L",
        "C",
        "K",
        "E",
        "T",
    )

    choice = random.randint(10000000, 99999999)
    letter = POSSIBLE_LETTERS[choice % 23]
    print(color.white + f'\n[&] The generated DNI is: {color.blue}{choice}{letter}')

    ret()

def id_info():
    try:
        user = input(color.white + '\n[&] Enter the user ID: ')
        url = f"https://discordlookup.mesalytic.moe/v1/user/{user}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            def format_user_info(data, indent=0):
                info = []
                for key, value in data.items():
                    if isinstance(value, dict):
                        info.append("  " * indent + f"{key.replace('_', ' ').title()}:")
                        info.append(format_user_info(value, indent + 1))
                    else:
                        if isinstance(value, list):
                            value = ", ".join(str(v) for v in value)
                        info.append("  " * indent + f"{key.replace('_', ' ').title()}: {value}")
                return '\n'.join(info)
            
            user_info = format_user_info(data)
            print(color.red + '\n[&] User info:\n-------------------------------------------------------------------------------')
            print(color.white + user_info)
            print(color.red + '\n-------------------------------------------------------------------------------' + color.RESET)
            
        else:
            print(color.BLUE + f'[>] Error: The response not arrrived. Status code: {response.status_code}')

    except:
        error()

    ret()

def main():
    clear()
    title = '''
                                         ___________ ______  _________       _______ _______                    
                                         \__    ___/    |   \______   \  ! |/ _|   \_   ___ \     
                                         |    |  |    |   /|       _/      < |   /    \  \/     
                                         |    |  |    |  / |    |   \    |  \|   \     \____    
                                         |____|  |______/  |____|_  /____|__ \___|\______  /    
                                                                  \/        \/           \/     
                                                                                                                    
                    -------------------------------------[TURKIC Multitool]--------------------------------------
'''

    for i in title:
        sys.stdout.flush()
        print(color.red + i,end="")
        time.sleep(0.001)   

    options = '''
    [00]: Exit the program                                [11]: Generate a sure password                  [22]: Change color theme to green    
    [01]: Get my IP address                               [12]: Read PDF file                             [23]: Socket port scanning to a target
    [02]: Verify the Internet connection                  [13]: Mask an URL                               [24]: Scan the ports of my computer
    [03]: Send Discord message                            [14]: Encrypt plain text with base64            [25]: Generate a false DNI
    [04]: Generate false IP address                       [15]: Obtener el espacio que ocupa un archivo   [26]: Discord ID info
    [05]: Generate false phone number                     [16]: Generate the QR Code of a URL
    [06]: Send WhatsApp message                           [17]: Clear the browser history
    [07]: Convert a plain text message in binary code     [18]: Download mp3 audio of a YouTube video
    [08]: View parrot.live                                [19]: Download mp4 video of YouTube
    [09]: Credits and info about this proyect             [20]: Generate a table with false user data
    [10]: Get my public IP address                        [21]: Read XSS vulnerable sites DataBase
'''
    for i in options:
        sys.stdout.flush()
        print(color.white + i,end="")
        time.sleep(0.001)

    print(color.red + f'\n┌── <{hostname}@Turkic-Multitool> ─ [~]')
    choice = input('└──╼ $ ')

    if choice == '00': exit()
    elif choice == '01': get_ip()
    elif choice == '02': verify()
    elif choice == '03': send_discord()
    elif choice == '04': gen_ip()
    elif choice == '05': gen_phone()
    elif choice == '06': send_whatsapp()
    elif choice == '07': binary()
    elif choice == '08': parrot()
    elif choice == '09': info()
    elif choice == '10': get_public()
    elif choice == '11': generate_pass()
    elif choice == '12': read_pdf()
    elif choice == '13': mask_url()
    elif choice == '14': enc_base64()
    elif choice == '15': get_size()
    elif choice == '16': qr_code()
    elif choice == '17': history()
    elif choice == '18': mp3()
    elif choice == '19': mp4()
    elif choice == '20': table()
    elif choice == '21': read()
    elif choice == '27': change_theme()
    elif choice == '23': scanner()
    elif choice == '24': system_scanner()
    elif choice == '25': gen_dni()
    elif choice == '26': id_info()
    else: error()

try:   
    main()

except:
    error()
