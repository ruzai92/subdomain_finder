import dns.resolver
import sys
import requests

domain = sys.argv[1]
url = "https://raw.githubusercontent.com/rbsec/dnscan/refs/heads/master/subdomains.txt"

def main():
    subdomain_store = []

    response = requests.get(url)
    response.raise_for_status()

    subdomains = response.text.splitlines()
    subdomains = [line.strip() for line in subdomains if line.strip()]

    for subdom in subdomains:
        try:
            ip_value = dns.resolver.resolve(f'{subdom}.{domain}','A')
            if ip_value:
                subdomain_store.append(f'{subdom}.{domain}')
                if f"{subdom}.{domain}" in subdomain_store:
                    print(f'{subdom}.{domain} valid')
                else:
                    pass
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.LifetimeTimeout:
            pass
        except KeyboardInterrupt:
            quit()

main()


