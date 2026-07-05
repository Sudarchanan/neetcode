class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ''
        else:
            res =''

            for item in strs:
                res = res +str(len(item))
                res = res + ','
            res = res + '/'

            for item in strs:
                res += item
            print(res)
            return res

    def decode(self, s: str) -> List[str]:

        if s == 'None':
            return []
        
        else:
            sizes = ''
            strss = ''
            res = []

            c = s.find('/')

            sizes = s[:c].split(',')[:-1]
            strss = s[c+1:]
            print(s)
            print(sizes, strss)
            
            i = 0
            
            for num in sizes :
                len = int(num)
                word = strss[i:len + i]
                i +=len
                res.append(word)
            return res



