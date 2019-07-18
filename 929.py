def numUniqueEmails(emails):
    remails = set()
    for email in emails:
        x, domain = email.split('@')
        y = x.split('+')[0].replace('.', '')
        remails.add(y + '@' + domain)
    print(len(remails))




if __name__ == "__main__":
    numUniqueEmails(["test.e.mail+bob.cathy@leetcode.com"])


