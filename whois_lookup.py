import whois


domain = input("Enter a domain name: ")
result = whois.whois(domain)
print(result)