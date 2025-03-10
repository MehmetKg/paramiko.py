import paramiko


def sendCommand(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    cmd_output = stdout.read()
    print(">>", cmd_output.decode())


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip = 'target_ip_adress'  # Kendi makinen
port = 22 # SSH portu
username = 'kendi_kullanıcı_adın'
password = 'kendi_şifren'


try:
    ssh.connect(ip, port=port, username=username, password=password)
    print(f"[+] Bağlantı başarılı: {ip}")

    command = input(">> ")
    while command.lower().strip() != "quit":
        if command.strip():
            sendCommand(ssh, command)
        command = input(">> ")

except Exception as e:
    print(f"[-] Hata oluştu: {e}")

finally:
    ssh.close()
    print("[+] Bağlantı kapatıldı.")
