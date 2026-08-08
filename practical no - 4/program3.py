server_ip = ("192.168.1.10")
allowed_ips = ["192.168.1.1","192.168.1.2"]

def update_allowed_ip(new_ip):
    allowed_ips.append(new_ip)
    print("Allowed ip added sucessfully.")
    
print("Server Ip : ", server_ip)
print("Allowed IPS : ", allowed_ips)

update_allowed_ip("192.168.1.3")

print("\n Update Configuration : ")
print("Server Ip : ", server_ip)
print("Allowed Ips : ", allowed_ips)