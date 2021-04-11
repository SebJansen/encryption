import unittest

from lib import calc_d, calc_n, calc_k, calc_e


class MyTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.p = 41
        self.q = 37
        self.n = calc_n(self.p, self.q)
        self.k = calc_k(self.p, self.q)
        self.e = calc_e(self.p, self.q, self.n, self.k)
        self.d = calc_d(self.e, self.k)

        self.message = 365
        self.enc = self.message ** self.e % self.n
        self.dec = self.enc ** self.d % self.n

    def test_decryption(self):
        self.assertEqual(self.message, self.dec)


if __name__ == '__main__':
    unittest.main()
