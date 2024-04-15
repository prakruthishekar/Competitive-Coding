# Input: emails = ["test.email+alex@leetcode.com",
#                  "test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and
# "testemail@lee.tcode.com" actually receive mails.


def numUniqueEmails(emails) -> int:
    res = ""
    uniqueEmail = set()
    for str in emails:
        a = str.split("@")
        a[0] = a[0].split("+")[0].replace(".", "")
        res = a[0] + "@" + a[1]
        uniqueEmail.add(res)
        res = ""
    
    return len(uniqueEmail)






print(numUniqueEmails(["test.email+alex@leetcode.com",
                       "test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))