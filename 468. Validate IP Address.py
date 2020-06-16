class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP and not ':' in IP:
            temp = IP.split('.')
            
            if not len(temp) == 4:
                return 'Neither'
            
            for i in temp:
                
                if not i.isdigit():
                    return 'Neither'
                
                if not 0 <= int(i) <= 255 or not i.isdigit() or i[0] == '0' and len(i) > 1:
                    return 'Neither'
                    
            return 'IPv4'
        
        elif ':' in IP and not '.' in IP: 
            
            if '::' in IP:
                return 'Neither'
            
            temp = IP.split(':')
            
            if not len(temp) == 8:
                return 'Neither'
            
            for i in temp:
                
                if len(i) > 4:
                    return 'Neither'
                
                for j in i:
                    
                    if not j.isdigit() and not j.isalpha(): 
                        return 'Neither'
                    
                    if j.isalpha():
                        if j.lower() >= 'g' and j.lower() <= 'z':
                            return 'Neither'
                    
            return 'IPv6'

        return 'Neither'
