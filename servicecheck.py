# import os

# service = "nginx"

# status = os.system(f"systemctl is-active --quiet {service}")

# if (status == 0):
#     print(f"The {service} service is active")
# else:
#     print(f"The {service} is not active")

#Since systemctl is not recognised in windows, we can't check nginx service is running ot not. So for the demonstartion ,i'm using windows based service below.



import os

service = "winDefend" #This is a window's service

status = os.system(f'sc query "{service}" | find "RUNNING"')

if (status == 0):
    print(f"The {service} service is active")
else:
    print(f"The {service} is not active")
