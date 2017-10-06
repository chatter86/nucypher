import unittest
from npre import umbral
from npre import elliptic_curve as ec
from nkms.crypto.crypto import Crypto


class TestCrypto(unittest.TestCase):
    def setUp(self):
        self.pre = umbral.PRE()
        self.privkey_a = self.pre.gen_priv()
        self.privkey_b = self.pre.gen_priv()

    def test_priv_bytes2ec(self):
        privkey_bytes = ec.serialize(self.privkey_a)[1:]
        self.assertEqual(bytes, type(privkey_bytes))
        self.assertEqual(32, len(privkey_bytes))

        privkey = Crypto.priv_bytes2ec(privkey_bytes)
        self.assertEqual(ec.ec_element, type(privkey))
        self.assertEqual(self.privkey_a, privkey)

    def test_pub_bytes2ec(self):
        pubkey = self.pre.priv2pub(self.privkey_a)
        self.assertEqual(ec.ec_element, type(pubkey))

        pubkey_bytes = ec.serialize(pubkey)[1:]
        self.assertEqual(bytes, type(pubkey_bytes))
        self.assertEqual(33, len(pubkey_bytes))

        pubkey_ec = Crypto.pub_bytes2ec(pubkey_bytes)
        self.assertEqual(ec.ec_element, type(pubkey_ec))
        self.assertEqual(pubkey_ec, pubkey)
