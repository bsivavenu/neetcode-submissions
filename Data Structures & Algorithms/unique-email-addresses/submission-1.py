class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = set()
        for email in emails:
            local , domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            unique_email.add(local+'@'+domain)
            print(unique_email)
        return len(unique_email)
