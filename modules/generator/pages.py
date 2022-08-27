from modules.config import charset
from ezzthread import threaded


def encode(n):
    try:
        return charset[n]
    except IndexError:
        raise Exception(f"Cannot encode {n}")


def decode(s):
    try:
        return charset.index(s)
    except ValueError:
        raise Exception(f"Cannot decode {s}")


def dec_to_base(dec=0, base=16):
    if dec < base:
        return encode(dec)
    else:
        return dec_to_base(dec // base, base) + encode(dec % base)


def base_to_dec(s, base=16, rec_pow=0):
    if s == str():
        return 0
    else:
        return decode(s[-1]) * (base ** rec_pow) + base_to_dec(s[0:-1], base, rec_pow + 1)


class Page:
    @staticmethod
    def from_index(index: int) -> str:
        return dec_to_base(index, len(charset))


class Index:
    @staticmethod
    def from_page(page: str) -> int:
        return base_to_dec(page, len(charset))
