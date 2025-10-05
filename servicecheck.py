import os

service = "nginx"

status = os.system(f"systemctl is-active --quiet {service}")

if (status == 0):
    print(f"The {service} service is active")
else:
    print(f"The {service} is not active")