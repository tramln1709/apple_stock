import logging
import os.path
import unittest
from functools import reduce

import util as U
import constants as C


class TestCase(unittest.TestCase):
    REGRESSION_DIR = "regression"

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        path = self.__class__.__module__.split('.')[1:]
        path = [C.PROJECT_DIR, self.REGRESSION_DIR] + path
        class_dir = reduce(os.path.join, path)
        test_dir = os.path.join(class_dir, "test")
        gold_dir = os.path.join(class_dir, "gold")

        for dir in [class_dir, gold_dir, test_dir]:
            if not os.path.isdir(dir):
                try:
                    os.makedirs(dir)
                except Exception as e:
                    print(e)

        test_name = self.simplify_test_name(self._testMethodName)
        self.test_file_name = os.path.join(test_dir, "{}.log".format(test_name))
        self.gold_file_name = os.path.join(gold_dir, "{}.log".format(test_name))
        self.diff_file_name = os.path.join(class_dir, "{}.diff.log".format(test_name))

    def tearDown(self) -> None:
        logging.disable(logging.NOTSET)
        if self.gold_file_name and os.path.isfile(self.gold_file_name):
            self.assertTrue(self.diff())

    def diff(self):
        command = "diff {} {}".format(self.test_file_name, self.gold_file_name)
        try:
            result = U.exec_shell_cmd(command)
        except Exception as e:
            result = e
            return False
        finally:
            self.log(result, self.diff_file_name)

        return len(result) == 0

    def log(self, message, path=None):
        path = path if path else self.test_file_name
        with open(path, "w") as _file:
            _file.write(str(message))

    def simplify_test_name(self, name):
        return name.replace("test_", "")
