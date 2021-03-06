# effectivepython

Effective Python のコードメモ


### 第1章: パイソニック思考(Pythonic Thinking)

1. [使っているPythonバージョンを知ろう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec01_version.py)
2. [PEP 8 スタイルガイドに従おう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec02_pep8.py)
3. [bytes, str, unicodeの違いを知ろう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec03_bytes_str.py)
4. [複雑な式の代わりにヘルパ関数を書こう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec04_helper_url.py)
5. [シーケンスのスライス方法を知ろう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec05_sequence_slice.py)
6. [単一のスライスではstart, end, stride利用を避ける](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec06_slice_stride.py)
7. [mapやfilterの代わりにリスト内包表記を使おう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec07_list_comprehension.p)
8. [リスト内包表記では2個以上の式を避ける](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec08_duplicate_list_comprehension.py)
9. [大きな内包ではジェネレータ式を検討しよう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec09_generator_expression.py)
10. [rangeよりもenumerateを使おう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec10_enumerate_list.py)
11. [複数イテレータを同時処理するならzipを使おう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec11_iterator_zip.py)
12. [for, whileループ後のelseブロックは避ける](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec12_README.md)
13. [try/except/else/finallyブロックをそれぞれ活用しよう](https://github.com/ku2ma2/effectivepython/blob/master/chapter01/sec13_try_except_block.py)

### 第2章: 関数(Functions)

14. [Noneを返すよりも例外を使おう](https://github.com/ku2ma2/effectivepython/blob/master/chapter02/sec14_exception_is_preferable.py)
15. [クロージャと変数スコープの関係を知ろう](https://github.com/ku2ma2/effectivepython/blob/master/chapter02/sec15_sort_priority.py)
16. [リストを返す代わりにジェネレータを検討しよう](https://github.com/ku2ma2/effectivepython/blob/master/chapter02/sec16_consider_generator.py)
17. [引数を介したイテレーションは防御的に行う](https://github.com/ku2ma2/effectivepython/blob/master/chapter02/sec17_defensive_iterator.py)
18. [可変長引数で視認性をあげる](https://github.com/ku2ma2/effectivepython/blob/master/chapter02/sec18_positional_arguments.py)
19. [キーワード引数を使ってオプション機能を提供する](https://github.com/ku2ma2/effectivepython/blob/master/chapter02/sec19_keyword_arguments.py)
20. [動的デフォルト引数ではNoneとドキュメンテーション文字列(docstring)を使おう](https://github.com/ku2ma2/effectivepython/blob/master/chapter02/sec20_dynamic_arguments.py)
21. [キーワードのみの引数(keyword-only argument)を使って明確にする](https://github.com/ku2ma2/effectivepython/blob/master/chapter02/sec21_keyword_only_arguments.py)

### 3章　クラスと継承

22. [辞書やタプルで記録管理するよりもヘルパークラスを使う](https://github.com/ku2ma2/effectivepython/blob/master/chapter03/sec22_helper_class.py)
23. [単純なインタフェースにはクラスの代わりに関数を使う](https://github.com/ku2ma2/effectivepython/blob/master/chapter03/sec23_callable_class.py)
24. [@classmethodポリモルフィズムを使ってオブジェクトをジェネリックに](https://github.com/ku2ma2/effectivepython/blob/master/chapter03/sec24_classmethod_prolymorphism.py)
25. [親クラスを superを使って初期化する](https://github.com/ku2ma2/effectivepython/blob/master/chapter03/sec25_super_class.py)
26. [多重継承は mix-inユーティリティクラスだけに使う](https://github.com/ku2ma2/effectivepython/blob/master/chapter03/sec26_mixin.py)
27. [プライベート属性よりはパブリック属性が好ましい](https://github.com/ku2ma2/effectivepython/blob/master/chapter03/sec27_public.py)
28. [カスタムコンテナ型は collections.abcを継承する](https://github.com/ku2ma2/effectivepython/blob/master/chapter03/sec28_collections.py)

### 4章 メタクラスと属性

29. [getやsetメソッドよりも素のままの属性を使う](https://github.com/ku2ma2/effectivepython/blob/master/chapter04/sec29_plain_attributes.py)
30. [属性をリファクタリングする代わりに @propertyを考える](https://github.com/ku2ma2/effectivepython/blob/master/chapter04/sec30_consider_property.py)
31. [再利用可能な @propertyメソッドにディスクリプタを使う](https://github.com/ku2ma2/effectivepython/blob/master/chapter04/sec31_reusable_property.py)
32. [遅延属性には \_\_getattr\_\_, \_\_getattribute\_\_, \_\_setattr\_\_を使う](https://github.com/ku2ma2/effectivepython/blob/master/chapter04/sec32_lazy_attributes.py)
33. [サブクラスをメタクラスで検証する](https://github.com/ku2ma2/effectivepython/blob/master/chapter04/sec33_meta_class.py)
34. [クラスの存在をメタクラスで登録する](https://github.com/ku2ma2/effectivepython/blob/master/chapter04/sec34_class_existence.py)
35. [クラス属性をメタクラスで注釈する](https://github.com/ku2ma2/effectivepython/blob/master/chapter04/sec35_class_attributes.py)

### 5章 並行性と並列性

36. [subprocessを使って子プロセスを管理する](https://github.com/ku2ma2/effectivepython/blob/master/chapter05/sec36_subprocess.py)
37. スレッドはブロッキング I/Oに使い、並列性に使うのは避ける
38. スレッドでのデータ競合を防ぐために Lockを使う
39. スレッド間の協調作業には Queueを使う
40. 多くの関数を並行に実行するにはコルーチンを考える
41. 本当の並列性のために concurrent.futuresを考える 


