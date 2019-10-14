import sys

def installer(package):
    print('Installing..', package)
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    from bs4 import BeautifulSoup
    print('BeautifulSoup is already installed...')
except ImportError:
    installer('beautifulsoup4')

try:
    import requests
    print('Requests is already installed...')
except ImportError:
    installer('requests')

print('All requirements satisfied...')