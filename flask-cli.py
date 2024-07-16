#!/usr/bin/env python3
import os
import argparse
from flask_app import app  # Import your Flask app

# Function to display a banner
def print_banner():
    banner = """
███╗   ██╗ █████╗ ██████╗ ███████╗ ██████╗ ███████╗████████╗
████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔═══██╗██╔════╝╚══██╔══╝
██╔██╗ ██║███████║██║  ██║███████╗██║   ██║█████╗     ██║   
██║╚██╗██║██╔══██║██║  ██║╚════██║██║   ██║██╔══╝     ██║   
██║ ╚████║██║  ██║██████╔╝███████║╚██████╔╝██║        ██║   
╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝        ╚═╝   
            ( Better software for everybody )      
    A powerful tool for creating a tunnel to your PC.                                     
    """
    print(banner)
    description = ['Terminal access', 'File sharing option', 'File download access']
    for item in description:
        print('[+] '+item) 

parser = argparse.ArgumentParser(description='A powerful tool for make a tunnel to your computer. Run the application to go crazy.')
parser.add_argument('directory', type=str, help='Directory to host the Flask app.')
parser.add_argument('-v', '--version', action='version', version='1.0', help='Show version information')
args = parser.parse_args()

BASE_DIR = os.path.abspath(args.directory)

if __name__ == '__main__':
    print_banner()  # Display the banner
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
