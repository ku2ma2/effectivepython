"""
項目3: bytes,str,unicodeの違いを知っておく
"""


def to_str(bytes_or_str):
    """
    文字列(str)に変更
    バイナリ(bytes)か文字列(str)かが分からない状態で bytes_or_str が
    与えられてバイナリだった場合は文字列にして返す
    """
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode('utf-8')

    return bytes_or_str


def to_bytes(bytes_or_str):
    """
    バイナリ(bytes)に変更
    バイナリ(bytes)か文字列(str)かが分からない状態で bytes_or_str が
    与えられてstr型だった場合はバイナリ(bytes)にして返す
    """
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode('utf-8')

    return bytes_or_str


def main():
    """
    直接実行された場合のメイン関数
    """
    print(type('str'))
    print(type(b'byte'))


if __name__ == "__main__":
    main()
