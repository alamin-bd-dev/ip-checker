import requests
import requests
import os

logo =[

    "\n||  __      __        ___   __        ___  __ "
    "\n|| |__)    /  ` |__| |__   /  ` |__/ |__  |__) "
    "\n|| |       \\__, |  | |___  \\__, |  \\ |___ |  \\ "
    "\n"
    "\n __________________Al Amin________________________"
    "\n___________________________________________________"
    "\n"
    "\n"
    "\n  IP Information Checker"
    "\n -----------------------"
    "\n"
    "\nThis tool uses IP-API to fetch geolocation information from a public IP address."
    "\n"
    "\n        Features"
    "\n -----------------------"
    "\n - Get country"
    "\n - Get city"
    "\n - Get ISP"
    "\n - Get latitude & longitude"
    "\n==================================================================="
    
    ]   
   
width = os.get_terminal_size().columns

for line in logo:
    print(line.center(width))

while True:
    print("""
 1. If you want IP details
 2. If you want to exit
 """)

    choice = input("What do you want?: ")

    if not choice.isdigit():
        print("Please enter numbers only!")
        continue

    if choice == '1':
        ip = input("Enter your IP: ")

        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        try:
            response = requests.get(url, timeout=5)
            data = response.json()
        except requests.exceptions.RequestException:
            print("Network error! Check your internet connection.")
            continue
        except ValueError:
            print("Invalid response from server!")
            continue
        
        if data.get("status") == "fail":
            print("Invalid IP address! Try again.")
            continue

        print("IP:", data.get("query"))
        print("Country:", data.get("country"))
        print("City:", data.get("city"))
        print("ISP:", data.get("isp"))
        print("Latitude:", data.get("lat"))
        print("Longitude:", data.get("lon"))

    elif choice == '2':
        print("Good bye from our IP checker!")
        break
    else:
        print("Invalid choice! Try again.")