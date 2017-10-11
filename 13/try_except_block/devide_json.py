"""
項目13: try, except,else, finally の各ブロックを活用する

- try/finally 文では、tryブロックで例外が起きるかは関係なく必ず後処理を実行する
- elseは try記述を最小にして処理を分離して可読性をあげる
- elseは finallyの共通後処理前に追加作業をするのに便利
"""

import json
UNDEFINED = []


def devide_json(path: str):
    """
    入力されたリスト内の一番長い文字列を返す

    >>> devide_json(['one','two','three'])
    'three'

    """
    handle = open(path, 'r+')

    try:
        data = handle.read()
        op = json.loads(data)

        value = op['numerator'] / op['denominator']  # ZeroDivisionErrorが出るかも
        # とその前に op の中に何も入ってなければ　KeyErrorが出るわけだが…

    except ZeroDivisionError as e:
        return UNDEFINED

    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)  # IOError 起こすかも
        return value

    finally:
        handle.close()  # 常に最後はファイルハンドルを閉じる


if __name__ == "__main__":
    print(devide_json('test.json'))
