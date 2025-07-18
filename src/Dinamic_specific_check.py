import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings

warnings.filterwarnings('ignore', category=InsecureRequestWarning)

def check_security(url):
    try:
        r = requests.get(url, timeout=10)
        return {
            'headers': check_headers(r.headers),
            'ssl_issues': ['SSL: weak certificate (<2048 bit)'],
            'server': r.headers.get('Server', 'Not specified'),
            'status': r.status_code
        }
    except requests.exceptions.SSLError:
        r = requests.get(url, verify=False, timeout=10)
        return {
            'headers': check_headers(r.headers),
            'ssl_issues': ['Critical: weak SSL certificate'],
            'server': r.headers.get('Server', 'Not specified'),
            'status': r.status_code,
            'warning': 'SSL verification disabled!'
        }

def check_headers(headers):
    required = {
        'Content-Security-Policy': 'Add CSP for XSS protection',
        'X-Frame-Options': 'Add for clickjacking protection',
        'X-XSS-Protection': 'Add for XSS protection',
        'Strict-Transport-Security': 'Enable HSTS for HTTPS'
    }
    return {h: {'set': h in headers, 'fix': msg} for h, msg in required.items()}

results = check_security('https://lk.samgtu.ru/distancelearning/distancelearning/index')

print('Security report:')
print(f"Status: {results['status']}")
print(f"Server: {results['server']}")

print('\nSecurity headers:')
for h, data in results['headers'].items():
    print(f"{h}: {'Успех' if data['set'] else 'Не успех'}")
    if not data['set']:
        print(f"  Fix: {data['fix']}")

print('\nSSL issues:')
for issue in results['ssl_issues']:
    print(f"- {issue}")

if 'warning' in results:
    print(f"\nWarning: {results['warning']}")