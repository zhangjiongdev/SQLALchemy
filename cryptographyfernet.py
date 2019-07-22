from cryptography.fernet import Fernet

class Crypto(object):
    """docstring for ClassName"""
    def __init__(self, key):
        self.factory = Fernet(key)
    def generate_key(self):
        key = Fernet.generate_key()
        print(key)
    # 加密
    def encrypt(self,string):
        token = self.factory.encrypt(string.encode('utf-8'))
        return token
    # 解密
    def decrypt(self,token):
        string = self.factory.decrypt(token).decode('utf-8')
        return string

# 密钥，需要保存好
key = b'GqycX8dOsZThS25NRI7hwCJw3JcKebj8NnXfVvqRHSc='
crypto = Crypto(key)

if __name__ == '__main__':
    # 加密字符串
    token = crypto.encrypt('A really secret message. Not for prying eyes.')
    print(token)
    # 解密字符串
    string = crypto.decrypt(token)
    print(string)