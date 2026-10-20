server = "AWS"
cpu = 75
print(f"Server {server} has {cpu}% CPU usage")
# Calculations inside f-strings
cpu = 40
memory = 30
print(f"total resource usage:{cpu+memory}%")
print(f"Double CPu Usage:{cpu*2}%")
# Decimal formatting
cpu = 76.6789
print(f"CPU Usage : {cpu:.2f}")
price = 1250.5
print(f"Price : {price:,.2f}")
# challenge
server = "AWS"
cpu = 82.567
memory = 67.234
print(f"{server} CPU: {cpu:.2f}%")
print(f"{server} Memory: {memory:.2f}%")
# Expressions and formatting together
cpu = 75
memory = 60
print(f"Average resource usage:{(cpu+memory)/2:.2f}")
# try
price  =2500
quantity = 3
print(f"Total bill: ₹{price*quantity:,.2f}")
# F-strings with expressions and methods
server = "aws production"
cpu = 75

print(f"Server: {server.upper()}")
print(f"CPU remaining: {100 - cpu}%")
print(f"Status: {'High' if cpu > 70 else 'Normal'}")
# F-strings with expressions and methods
service = "docker"
usage = 45
print(f"Service: {service.upper()}")
print(f"reamining Capacity: {10+45}%")
# Final challenge
server = "aws"
cpu = 82.567
memory = 64.234
status = "running"

print(f"SERVER: {server.upper()}")
print(f"CPU Usage: {cpu:.2f}%")
print(f"Memory Usage: {memory:.2f}%")
print(f"Status: {status.upper()}")
