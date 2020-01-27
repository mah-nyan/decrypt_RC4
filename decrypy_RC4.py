from Crypto.Cipher import ARC4

key = 'KAREEM'
enc = bytes.fromhex('afdd793b510967cd50af8324bcf19c335ad046ec')

cipher = ARC4.new(key)
dec = cipher.decrypt(enc)
print(dec)
