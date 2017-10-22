import nacl.encoding
import nacl.hash
from nacl.bindings.utils import sodium_memcmp

HASHER = nacl.hash.sha256
# could be nacl.hash.sha512 or nacl.hash.blake2b instead

# define a 1024 bytes log message
msg = 16*b'256 BytesMessage'
digest = HASHER(msg, encoder=nacl.encoding.HexEncoder)

# now send msg and digest to the user
print(nacl.encoding.HexEncoder.encode(msg))
print(digest)

HASHER = nacl.hash.sha256
# could be nacl.hash.sha512 or nacl.hash.blake2b instead

# we received a 1024 bytes long message and it hex encoded digest
received_msg = nacl.encoding.HexEncoder.decode(
b'3235362042797465734d6573736167653235362042797465734d657373616765'
b'3235362042797465734d6573736167653235362042797465734d657373616765'
b'3235362042797465734d6573736167653235362042797465734d657373616765'
b'3235362042797465734d6573736167653235362042797465734d657373616765'
b'3235362042797465734d6573736167653235362042797465734d657373616765'
b'3235362042797465734d6573736167653235362042797465734d657373616765'
b'3235362042797465734d6573736167653235362042797465734d657373616765'
b'3235362042797465734d6573736167653235362042797465734d657373616765'
)

dgst = b'12b413c70c148d79bb57a1542156c5f35e24ad77c38e8c0e776d055e827cdd45'

shortened = received_msg[:-1]
modified = b'modified' + received_msg[:-8]

orig_dgs = HASHER(received_msg, encoder=nacl.encoding.HexEncoder)
shrt_dgs = HASHER(shortened, encoder=nacl.encoding.HexEncoder)
mdfd_dgs = HASHER(modified, encoder=nacl.encoding.HexEncoder)

def eq_chk(dgs0, dgs1):
    if sodium_memcmp(dgs0, dgs1):
        return 'equals'
    return 'is different from'

MSG = 'Digest of {0} message {1} original digest'

for chk in (('original', orig_dgs),
            ('truncated', shrt_dgs),
            ('modified', mdfd_dgs)):

    print(MSG.format(chk[0], eq_chk(dgst, chk[1])))
