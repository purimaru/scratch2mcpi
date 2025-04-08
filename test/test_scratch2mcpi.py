import unittest
import sys
import os

# is_number 関数を scratch2mcpi.py からコピーしてテスト対象とします。
# (元のスクリプトを直接インポートすると意図しない動作を引き起こす可能性があるため)
def is_number(value):
    """
    渡された値が整数または浮動小数点数であるかを確認します。
    注意: Pythonではboolはintのサブクラスであるため、isinstance(True, int) は True となります。
    この関数はその挙動を反映しています。
    """
    if (isinstance(value, (int, float))):
        return True
    else:
        return False

class TestIsNumber(unittest.TestCase):

    def test_integer_input(self):
        """整数が渡された場合にTrueを返すことをテスト"""
        self.assertTrue(is_number(10), "正の整数で失敗")
        self.assertTrue(is_number(0), "ゼロで失敗")
        self.assertTrue(is_number(-5), "負の整数で失敗")

    def test_float_input(self):
        """浮動小数点数が渡された場合にTrueを返すことをテスト"""
        self.assertTrue(is_number(3.14), "正の小数で失敗")
        self.assertTrue(is_number(0.0), "ゼロの小数で失敗")
        self.assertTrue(is_number(-2.71), "負の小数で失敗")

    def test_string_input(self):
        """文字列が渡された場合にFalseを返すことをテスト"""
        self.assertFalse(is_number("10"), "数字の文字列で失敗")
        self.assertFalse(is_number("abc"), "アルファベットの文字列で失敗")
        self.assertFalse(is_number(""), "空文字列で失敗")

    def test_boolean_input(self):
        """ブール値が渡された場合にTrueを返すことをテスト (boolはintのサブクラスであるため)"""
        self.assertTrue(is_number(True), "Trueの場合に失敗 (isinstanceの挙動によりTrueが期待される)")
        self.assertTrue(is_number(False), "Falseの場合に失敗 (isinstanceの挙動によりTrueが期待される)")
        # もしboolを数値として扱わない場合は、以下のようにFalseを期待するべきです:
        # self.assertFalse(is_number(True), "Trueの場合に失敗 (Falseが期待される)")
        # self.assertFalse(is_number(False), "Falseの場合に失敗 (Falseが期待される)")

    def test_none_input(self):
        """Noneが渡された場合にFalseを返すことをテスト"""
        self.assertFalse(is_number(None), "Noneの場合に失敗")

    def test_list_input(self):
        """リストが渡された場合にFalseを返すことをテスト"""
        self.assertFalse(is_number([1, 2]), "リストの場合に失敗")

    def test_dict_input(self):
        """辞書が渡された場合にFalseを返すことをテスト"""
        self.assertFalse(is_number({"a": 1}), "辞書の場合に失敗")

if __name__ == '__main__':
    # このファイルから直接テストを実行できるようにします
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
