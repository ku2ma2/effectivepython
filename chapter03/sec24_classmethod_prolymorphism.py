"""
項目24: @classmethod でポリモーフィズムしてオブジェクトをジェネリックに構築する

Use @classmethod Polymorphism to Construct Objects Generically

- Pythonは、クラスに対して __init__メソッドという1つのコンストラクタしかサポートしていない。
- クラスに対して、代わりのコンストラクタを定義するために@classmethodを使う
- 具体化したサブクラスを作成して連携するジェネリックな方式を提供するには、クラスメソッドポリモーフィズムを使う

"""


class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


if __name__ == "__main__":
    pass
