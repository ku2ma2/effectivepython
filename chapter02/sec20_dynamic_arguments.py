"""
項目20: 動的なデフォルト引数を指定するときはNoneとdocstringsを使う

Use None and Docstrings to Specify Dynamic Default Arguments

- 関数の引数は、位置またはキーワードによって指定可能
- キーワード引数は、位置引数だけでは紛らわしい場合に、各引数の目的を明確にする
- デフォルト値を設定したキーワード引数は、関数が別の場所に使われている状態でも新たな振る舞いを追加する事を容易にする
- オプション(あってもなくても良い)のキーワード引数は位置ではなくキーワードで常に渡すべきである
"""

from datetime import datetime


def log_message(message, when=None):
    """
    ログメッセージを日時と同時に表示

    Args:
        message: 出力するメッセージ
        when: メッセージを出力した際のdatetime日時
              何も与えられない場合は利用された時点での日時
    """

    if when is None:
        when = datetime.now()

    return "{}: {}".format(message, when)


if __name__ == "__main__":
    print(log_message('aa'))
