import unittest
from skycoin_crypto import *


class TestSkycoinCrypto(unittest.TestCase):
    def test_sign(self):
        # TODO Rewrite this test
        # The signatures will be random every time, the only thing you can do
        # is verify that the signature is valid or not valid
        skycoin = SkycoinCrypto()
        digest = create_string_buffer(b'\x00\x1a\xa9\xe4\x16\xaf\xf5\xf3\xa3\xc7\xf9\xae\x08\x11\x75\x7c\xf5\x4f\x39\x3d\x50\xdf\x86\x1f\x5c\x33\x74\x79\x54\x34\x1a\xa7')
        seckey = create_string_buffer(b'\x59\x7e\x27\x36\x86\x56\xca\xb3\xc8\x2b\xfc\xf2\xfb\x07\x4c\xef\xd8\xb6\x10\x17\x81\xa2\x77\x09\xba\x1b\x32\x6b\x73\x8d\x2c\x5a')
        ret, sig = skycoin.SkycoinEcdsaSignDigest(seckey, digest)
        self.assertEqual(ret, 0)
        self.assertEqual(65, len(sig))
        ret, pubkey = skycoin.SkycoinEcdsaVerifyDigestRecover(sig, digest)
        self.assertEqual(ret, 0)
        expectPubkey = skycoin.SkycoinPubkeyFromSeckey(seckey)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(expectPubkey))

        digest = create_string_buffer(b'\x00\x1a\xa9\xe4\x16\xaf\xf5\xf3\xa3\xc7\xf9\xae\x08\x11\x75\x7c\xf5\x4f\x39\x3d\x50\xdf\x86\x1f\x5c\x33\x74\x79\x54\x34\x1a\xa7')
        seckey = create_string_buffer(b'\x67\xa3\x31\x66\x90\x81\xd2\x26\x24\xf1\x65\x12\xea\x61\xe1\xd4\x4c\xb3\xf2\x6a\xf3\x33\x39\x73\xd1\x7e\x0e\x8d\x03\x73\x3b\x78')
        ret, sig = skycoin.SkycoinEcdsaSignDigest(seckey, digest)
        self.assertEqual(ret, 0)
        self.assertEqual(65, len(sig))
        ret, pubkey = skycoin.SkycoinEcdsaVerifyDigestRecover(sig, digest)
        self.assertEqual(ret, 0)
        expectPubkey = skycoin.SkycoinPubkeyFromSeckey(seckey)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(expectPubkey))

    def test_sha256sum(self):
        skycoin = SkycoinCrypto()
        seed = create_string_buffer(b'seed')
        digest = skycoin.ComputeSha256Sum(seed)
        self.assertEqual(binascii.hexlify(digest), binascii.hexlify(b'\x19\xb2\x58\x56\xe1\xc1\x50\xca\x83\x4c\xff\xc8\xb5\x9b\x23\xad\xbd\x0e\xc0\x38\x9e\x58\xeb\x22\xb3\xb6\x47\x68\x09\x8d\x00\x2b'))

        seed = create_string_buffer(b'random_seed')
        digest = skycoin.ComputeSha256Sum(seed)
        self.assertEqual(binascii.hexlify(digest), binascii.hexlify(b'\x7b\x49\x1f\xac\xe1\x5c\x5b\xe4\x3d\xf3\xaf\xfe\x42\xe6\xe4\xaa\xb4\x85\x22\xa3\xb5\x64\x04\x3d\xe4\x64\xe8\xde\x50\x18\x4a\x5d'))

        seed = create_string_buffer(b'024f7fd15da6c7fc7d0410d184073ef702104f82452da9b3e3792db01a8b7907c3')
        digest = skycoin.ComputeSha256Sum(seed)
        self.assertEqual(binascii.hexlify(digest), binascii.hexlify(b'\xa5\xda\xa8\xc9\xd0\x3a\x9e\xc5\x00\x08\x8b\xdf\x01\x23\xa9\xd8\x65\x72\x5b\x03\x89\x5b\x12\x91\xf2\x55\x00\x73\x72\x98\xe0\xa9'))

    def test_generate_skycoin_pubkey_from_seckey(self):
        skycoin = SkycoinCrypto()
        seckey = create_string_buffer(b'\xa7\xe1\x30\x69\x41\x66\xcd\xb9\x5b\x1e\x1b\xbc\xe3\xf2\x1e\x4d\xbd\x63\xf4\x6d\xf4\x2b\x48\xc5\xa1\xf8\x29\x50\x33\xd5\x7d\x04')
        pubkey = skycoin.SkycoinPubkeyFromSeckey(seckey)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(b'\x02\x44\x35\x0f\xaa\x76\x79\x9f\xec\x03\xde\x2f\x32\x4a\xcd\x07\x7f\xd1\xb6\x86\xc3\xa8\x9b\xab\xc0\xef\x47\x09\x6c\xcc\x5a\x13\xfa'))

        seckey = create_string_buffer(b'\x00\x1a\xa9\xe4\x16\xaf\xf5\xf3\xa3\xc7\xf9\xae\x08\x11\x75\x7c\xf5\x4f\x39\x3d\x50\xdf\x86\x1f\x5c\x33\x74\x79\x54\x34\x1a\xa7')
        pubkey = skycoin.SkycoinPubkeyFromSeckey(seckey)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(b'\x02\xe5\xbe\x89\xfa\x16\x1b\xf6\xb0\xbc\x64\xec\x9e\xc7\xfe\x27\x31\x1f\xbb\x78\x94\x9c\x3e\xf9\x73\x9d\x4c\x73\xa8\x49\x20\xd6\xe1'))

        seckey = create_string_buffer(b'\xff\x67\x18\x60\xc5\x8a\xad\x3f\x76\x5d\x8a\xdd\x25\x04\x64\x12\xda\xbf\x64\x11\x86\x47\x2e\x15\x53\x43\x5e\x6e\x3c\x4a\x6f\xb0')
        pubkey = skycoin.SkycoinPubkeyFromSeckey(seckey)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(b'\x03\x0e\x40\xdd\xa2\x1c\x27\x12\x6d\x82\x9b\x6a\xe5\x78\x16\xe1\x44\x0d\xcb\x2c\xc7\x3e\x37\xe8\x60\xaf\x26\xef\xf1\xec\x55\xed\x73'))

        seckey = create_string_buffer(b'\x84\xfd\xc6\x49\x96\x4b\xf2\x99\xa7\x87\xcb\x78\xcd\x97\x59\x10\xe1\x97\xdb\xdd\xd7\xdb\x77\x6e\xce\x54\x4f\x41\xc4\x4b\x30\x56')
        pubkey = skycoin.SkycoinPubkeyFromSeckey(seckey)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(b'\x03\x58\x43\xe7\x22\x58\x69\x6b\x39\x1c\xf1\xd8\x98\xfc\x65\xf3\x1e\x66\x87\x6e\xa0\xc9\xe1\x01\xf8\xdd\xc3\xeb\xb4\xb8\x7d\xc5\xb0'))

    def test_base58_address_from_pubkey(self):
        skycoin = SkycoinCrypto()
        pubkey = create_string_buffer(b'\x02\xe5\xbe\x89\xfa\x16\x1b\xf6\xb0\xbc\x64\xec\x9e\xc7\xfe\x27\x31\x1f\xbb\x78\x94\x9c\x3e\xf9\x73\x9d\x4c\x73\xa8\x49\x20\xd6\xe1')
        address = skycoin.SkycoinAddressFromPubkey(pubkey)
        self.assertEqual(address.value, b"2EVNa4CK9SKosT4j1GEn8SuuUUEAXaHAMbM")
        self.assertEqual(skycoin.lib.strlen(address), 35)

    def test_recover_pubkey_from_signed_digest(self):
        skycoin = SkycoinCrypto()
        fingerprint = create_string_buffer(b'\xc3\x87\x6e\x66\x82\x6a\x54\x17\x21\x84\xd0\x7b\x65\x3b\xed\xe3\x04\xc3\xee\x6a\x15\x8d\x57\x68\x9d\xbf\x12\x72\x9c\xf1\x2c\x64')
        signature = create_string_buffer(b'\x79\xbe\x66\x7e\xf9\xdc\xbb\xac\x55\xa0\x62\x95\xce\x87\x0b\x07\x02\x9b\xfc\xdb\x2d\xce\x28\xd9\x59\xf2\x81\x5b\x16\xf8\x17\x98\x57\xfb\xb3\x34\x94\xfa\xcc\x02\xb8\x9a\xf1\x6c\x43\x88\x8e\xff\xf8\xfb\xc9\x18\xdc\xdb\xfa\x21\x46\x2c\x23\xf5\xa6\x41\x5b\x1d\x01')
        ret, pubkey = skycoin.SkycoinEcdsaVerifyDigestRecover(signature, fingerprint)
        self.assertEqual(ret, 0)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(b'\x03\xb1\x7c\x7b\x7c\x56\x43\x85\xbe\x66\xf9\xc1\xb9\xda\x6a\x0b\x5a\xea\x56\xf0\xcb\x70\x54\x8e\x65\x28\xa2\xf4\xf7\xb2\x72\x45\xd8'))

        fingerprint = create_string_buffer(b'\x17\x6b\x81\x62\x3c\xf9\x8f\x45\x87\x9f\x3a\x48\xfa\x34\xaf\x77\xdd\xe4\x4b\x2f\xfa\x0d\xdd\x2b\xf9\xed\xb3\x86\xf7\x6e\xc0\xef')
        signature = create_string_buffer(b'\x86\x4c\x6a\xbf\x85\x21\x4b\xe9\x9f\xed\x3d\xc3\x75\x91\xa7\x42\x82\xf5\x66\xfb\x52\xfb\x56\xab\x21\xda\xbc\x0d\x12\x0f\x29\xb8\x48\xff\xeb\x52\xa7\x84\x3a\x49\xc4\x11\x75\x3c\x0e\xdc\x12\xc0\xde\xdf\x63\x13\x26\x67\x22\xbe\xe9\x82\xa0\xd3\xb3\x84\xb6\x26')
        ret, pubkey = skycoin.SkycoinEcdsaVerifyDigestRecover(signature, fingerprint)
        self.assertEqual(ret, 0)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(b'\x03\xb1\x7c\x7b\x7c\x56\x43\x85\xbe\x66\xf9\xc1\xb9\xda\x6a\x0b\x5a\xea\x56\xf0\xcb\x70\x54\x8e\x65\x28\xa2\xf4\xf7\xb2\x72\x45\xd8'))

        fingerprint = create_string_buffer(b'\x17\x6b\x81\x62\x3c\xf9\x8f\x45\x87\x9f\x3a\x48\xfa\x34\xaf\x77\xdd\xe4\x4b\x2f\xfa\x0d\xdd\x2b\xf9\xed\xb3\x86\xf7\x6e\xc0\xef')
        signature = create_string_buffer(b'\x63\x11\x82\xb9\x72\x24\x89\xee\xdd\x1a\x9e\xab\x36\xbf\x77\x6c\x3e\x67\x9a\xa2\xb1\xbd\x3f\xb3\x46\xdb\x0f\x77\x6b\x98\x2b\xe2\x5b\xdd\x33\xd4\xe8\x93\xac\xa6\x19\xef\xf3\x01\x3e\x08\x73\x07\xd2\x2c\xa3\x06\x44\xc9\x6e\xa0\xfb\xde\xf0\x63\x96\xd1\xbf\x96')
        ret, pubkey = skycoin.SkycoinEcdsaVerifyDigestRecover(signature, fingerprint)
        self.assertEqual(ret, 0)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(b'\x03\x9f\x12\xc9\x36\x45\xe3\x5e\x52\x74\xdc\x38\xf1\x91\xbe\x0b\x6d\x13\x21\xec\x35\xd2\xd2\xa3\xdd\xf7\xd1\x3e\xd1\x2f\x6d\xa8\x5b'))

        fingerprint = create_string_buffer(b'\x17\x6b\x81\x62\x3c\xf9\x8f\x45\x87\x9f\x3a\x48\xfa\x34\xaf\x77\xdd\xe4\x4b\x2f\xfa\x0d\xdd\x2b\xf9\xed\xb3\x86\xf7\x6e\xc0\xef')
        signature = create_string_buffer(b'\xd2\xa8\xec\x2b\x29\xce\x3c\xf3\xe6\x04\x82\x96\x18\x8a\xdf\xf4\xb5\xdf\xcb\x33\x7c\x1d\x11\x57\xf2\x86\x54\xe4\x45\xbb\x94\x0b\x4e\x47\xd6\xb0\xc7\xba\x43\xd0\x72\xbf\x86\x18\x77\x5f\x12\x3a\x43\x5e\x8d\x1a\x15\x0c\xb3\x9b\xbb\x1a\xa8\x0d\xa8\xc5\x7e\xa1')
        ret, pubkey = skycoin.SkycoinEcdsaVerifyDigestRecover(signature, fingerprint)
        self.assertEqual(ret, 0)
        self.assertEqual(binascii.hexlify(pubkey), binascii.hexlify(b'\x03\x33\x8f\xfc\x0f\xf4\x2d\xf0\x7d\x27\xb0\xb4\x13\x1c\xd9\x6f\xfd\xfa\x46\x85\xb5\x56\x6a\xaf\xc7\xaa\x71\xed\x10\xfd\x1c\xbd\x6f'))

        # Skycoin core test vector: TestSigRecover2 1
        fingerprint = create_string_buffer(b'\x01\x6b\x81\x62\x3c\xf9\x8f\x45\x87\x9f\x3a\x48\xfa\x34\xaf\x77\xdd\xe4\x4b\x2f\xfa\x0d\xdd\x2b\xf9\xed\xb3\x86\xf7\x6e\xc0\xef')
        signature = create_string_buffer(b'\xd2\xa8\xec\x2b\x29\xce\x3c\xf3\xe6\x04\x82\x96\x18\x8a\xdf\xf4\xb5\xdf\xcb\x33\x7c\x1d\x11\x57\xf2\x86\x54\xe4\x45\xbb\x94\x0b\x4e\x47\xd6\xb0\xc7\xba\x43\xd0\x72\xbf\x86\x18\x77\x5f\x12\x3a\x43\x5e\x8d\x1a\x15\x0c\xb3\x9b\xbb\x1a\xa8\x0d\xa8\xc5\x7e\xa1')
        ret, pubkey = skycoin.SkycoinEcdsaVerifyDigestRecover(signature, fingerprint)
        self.assertEqual(ret, 0)
        self.assertEqual(binascii.hexlify(pubkey), '03c0b0e24d55255f7aefe3da7a947a63028b573f45356a9c22e9a3c103fd00c3d1')

        # Skycoin core test vector: TestSigRecover2 2
        fingerprint = create_string_buffer(b'\x17\x6b\x81\x62\x3c\xf9\x8f\x45\x87\x9f\x3a\x48\xfa\x34\xaf\x77\xdd\xe4\x4b\x2f\xfa\x0d\xdd\x2b\xf9\xed\xb3\x86\xf7\x6e\xc0\xef')
        signature = create_string_buffer(b'\xd2\xa8\xec\x2b\x20\xce\x3c\xf3\xe6\x04\x82\x96\x18\x8a\xdf\xf4\xb5\xdf\xcb\x33\x7c\x1d\x11\x57\xf2\x86\x54\xe4\x45\xbb\x94\x0b\x4e\x47\xd6\xb0\xc7\xba\x43\xd0\x72\xbf\x86\x18\x77\x5f\x12\x3a\x43\x5e\x8d\x1a\x15\x0c\xb3\x9b\xbb\x1a\xa8\x0d\xa8\xc5\x7e\xa1')
        ret, pubkey = skycoin.SkycoinEcdsaVerifyDigestRecover(signature, fingerprint)
        self.assertEqual(ret, 0)
        self.assertEqual(binascii.hexlify(pubkey), '03cee91b6d329e00c344ad5d67cfd00d885ec36e8975b5d9097738939cb8c08b31')

        # Skycoin core test vector: TestSigRecover2 3
        fingerprint = create_string_buffer(b'\x17\x6b\x81\x62\x3c\xf9\x8f\x45\x87\x9f\x3a\x48\xfa\x34\xaf\x77\xdd\xe4\x4b\x2f\xfa\x0d\xdd\x2b\xf9\xed\xb3\x86\xf7\x6e\xc0\xef')
        signature = create_string_buffer(b'\xd2\x01\xec\x2b\x29\xce\x3c\xf3\xe6\x04\x82\x96\x18\x8a\xdf\xf4\xb5\xdf\xcb\x33\x7c\x1d\x11\x57\xf2\x86\x54\xe4\x45\xbb\x94\x0b\x4e\x47\xd6\xb0\xc7\xba\x43\xd0\x72\xbf\x86\x18\x77\x5f\x12\x3a\x43\x5e\x8d\x1a\x15\x0c\xb3\x9b\xbb\x1a\xa8\x0d\xa8\xc5\x7e\xa1')
        ret, _ = skycoin.SkycoinEcdsaVerifyDigestRecover(signature, fingerprint)
        self.assertEqual(ret, 1)


if __name__ == '__main__':
    unittest.main()
