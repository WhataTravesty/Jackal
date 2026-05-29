import whois

def lookup_domain(domain):
    print(f"\nQuerying WHOIS for: {domain}\n")
    
    result = whois.whois(domain)
    
    print(f"Domain Name:    {result.domain_name}")
    print(f"Registrar:      {result.registrar}")
    print(f"Creation Date:  {result.creation_date}")
    print(f"Expiry Date:    {result.expiration_date}")
    print(f"Name Servers:   {result.name_servers}")
    print(f"Emails:         {result.emails}")
    print(f"Country:        {result.country}")

domain = input("Enter a domain to investigate: ")
lookup_domain(domain)