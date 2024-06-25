import subprocess
import time
import os

os.chdir('src')
mitmdump_process = subprocess.Popen(['mitmdump', '-s', 'requests.py'])
print('================ Running mitmdump ================')
time.sleep(2)
try:
    print('================ Running scrapes ================')
    subprocess.run(['python', 'scrapes.py'])
except Exception as e:
    print(f"Error running scraping script: {e}")
