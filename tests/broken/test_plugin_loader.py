# This test works on its own, but not as part of the CI

import shutil
import tempfile
import unittest

from gourmet import gglobals
from gourmet.plugin_loader import MasterLoader


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # preserve the current gourmet working directory
        cls.original_gourmetdir = gglobals.gourmetdir

        # create a temporary test directory
        cls.tmp_dir = tempfile.mkdtemp()
        gglobals.gourmetdir = cls.tmp_dir

        # Continue to import with 'gourmetdir' set to 'tmp_dir',
        # Tests need to setup their own test workspace, otherwise 'gourmetdir'
        # is set to '~/.gourmet' which could result in the user gourmet
        # database and other files being corrupted.
        # This isolation only works if this test is ran alone.

        cls.ml = MasterLoader.instance()

    @classmethod
    def tearDownClass(cls):
        # restore the original gourmet working directory location
        gglobals.gourmetdir = cls.original_gourmetdir

        # delete temporary test directory
        shutil.rmtree(cls.tmp_dir)

    def testDefaultPlugins(self):
        self.ml.load_active_plugins()
        print(f'active: {self.ml.active_plugins}')
        print(f'instantiated: {self.ml.instantiated_plugins}')
        # there should be 0 plugin errors
        self.assertEqual(len(self.ml.errors), 0)

    def testAvailablePlugins(self):
        # search module directories for available plugins
        for module_name, plugin_set in self.ml.available_plugin_sets.items():
            if module_name not in self.ml.active_plugin_sets:
                self.ml.activate_plugin_set(plugin_set)

        self.ml.save_active_plugins()

        # There should be 0 plugin errors
        self.assertEqual(len(self.ml.errors), 0)


if __name__ == '__main__':
    unittest.main()
