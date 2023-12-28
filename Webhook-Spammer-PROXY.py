import requests
import threading
import pystyle
from pystyle import Colors, Colorate
import time
import ctypes


def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


set_console_title("[- XENIHOOK - ] -!- [discord.gg/eV3sTyjd] ")
print(Colorate.Horizontal(Colors.red_to_purple, """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗  
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝  
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝   
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗   
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗  
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝  
                                                                Written By XeniDev [W/SyrupNk]
███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                  
""", 1))


def send_message_with_proxy(webhook_url, content, proxy):
    try:
        proxies = {'http': f'http://{proxy}'}
        data = {"content": content}
        response = requests.post(webhook_url, json=data, proxies=proxies, timeout=10)
        if response.status_code == 204:
            print(f"Message sent successfully using proxy: {proxy}")
        else:
            print(f"Failed to send message using proxy: {proxy}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error sending message using proxy: {proxy}. {str(e)}")

def send_messages_with_proxies(webhook_url, content, proxies, repetitions):
    threads = []
    max_threads = 5

    for _ in range(repetitions):
        for proxy in proxies:
            thread = threading.Thread(target=send_message_with_proxy, args=(webhook_url, content, proxy))
            threads.append(thread)
            thread.start()

            if len(threads) >= max_threads:
                for thread in threads:
                    thread.join()
                threads = []

 
    for thread in threads:
        thread.join()

def color_input(prompt, color):
    print(color + prompt)
    user_input = input()
    print('\033[0m', end='')  
    return user_input

def main():
    webhook_url = color_input("[>URL] ", '\033[91m')  
    message_content = color_input("[>CONTENT] ", '\033[91m')  

    proxies_list = [
    '185.249.107.84:3128',
    '185.229.111.106:45020',
    '67.43.227.227:25863',
    '218.57.210.186:9002'
#get your own proxies bruv
    ]
    send_messages_with_proxies(webhook_url, message_content, proxies_list, repetitions=750)

if __name__ == "__main__":
    main()
