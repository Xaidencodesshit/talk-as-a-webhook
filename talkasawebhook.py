import requests

BLUE = '\033[94m'
LIGHT_GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

logo = (
    BLUE + '                                                                                     \n' +
    '                                                                                     \n' +
    'XXXXXXX       XXXXXXX               AAA               IIIIIIIIIIDDDDDDDDDDDDD        \n' +
    'X:::::X       X:::::X              A:::A              I::::::::ID::::::::::::DDD     \n' +
    'X:::::X       X:::::X             A:::::A             I::::::::ID:::::::::::::::DD   \n' +
    'X::::::X     X::::::X            A:::::::A            II::::::IIDDD:::::DDDDD:::::D  \n' +
    'XXX:::::X   X:::::XXX           A:::::::::A             I::::I    D:::::D    D:::::D \n' +
    '   X:::::X X:::::X             A:::::A:::::A            I::::I    D:::::D     D:::::D\n' +
    '    X:::::X:::::X             A:::::A A:::::A           I::::I    D:::::D     D:::::D\n' +
    '     X:::::::::X             A:::::A   A:::::A          I::::I    D:::::D     D:::::D\n' +
    '     X:::::::::X            A:::::A     A:::::A         I::::I    D:::::D     D:::::D\n' +
    '    X:::::X:::::X          A:::::AAAAAAAAA:::::A        I::::I    D:::::D     D:::::D\n' +
    '   X:::::X X:::::X        A:::::::::::::::::::::A       I::::I    D:::::D     D:::::D\n' +
    'XXX:::::X   X:::::XXX    A:::::AAAAAAAAAAAAA:::::A      I::::I    D:::::D    D:::::D \n' +
    'X::::::X     X::::::X   A:::::A             A:::::A   II::::::IIDDD:::::DDDDD:::::D  \n' +
    'X:::::X       X:::::X  A:::::A               A:::::A  I::::::::ID:::::::::::::::DD   \n' +
    'X:::::X       X:::::X A:::::A                 A:::::A I::::::::ID::::::::::::DDD     \n' +
    'XXXXXXX       XXXXXXXAAAAAAA                   AAAAAAAIIIIIIIIIIDDDDDDDDDDDDD        \n' +
    '                                                                                     \n' +                                                                             
    RESET +
    LIGHT_GREEN + "Talk as a webhook\n" + RESET
)

def send_webhook_message(webhook_url, message):
    try:
        payload = {'content': message}
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  
        return True, response.status_code
    except requests.RequestException as e:
        return False, str(e)

def main():
    print(logo)

    webhook_url = None
    
    while True:
        if webhook_url is None:
            webhook_url = input(BLUE + "Enter the webhook URL: " + RESET)
        
        message = input(RED + "Enter the message to send: " + RESET)
        
        success, response = send_webhook_message(webhook_url, message)
        
        if success:
            print(LIGHT_GREEN + "Message sent successfully!" + RESET)
        else:
            print(RED + "Failed to send message:", response, RESET)
        
        again = input("Do you want to send another message? (y/n): ").strip().lower()
        if again != 'y':
            webhook_url = None
            break

if __name__ == "__main__":
    main()
