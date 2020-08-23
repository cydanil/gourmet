import os.path
from pathlib import Path
import sys

# The following lines are modified at installation time by setup.py so they
# point to the actual data files installation paths.

lib_dir = Path('gourmet')
data_dir = Path('data')
ui_base = Path('ui')
doc_base = Path('..')  # TODO: clean
locale_base = Path('../build/mo')  # TODO: clean
plugin_base = Path('../build/share/gourmet')  # TODO: clean

# Apologies for the formatting -- something in the build process is
# getting rid of indentations in this file which throws a syntax error
# on install
if getattr(sys, 'frozen', False): base_dir = os.path.dirname(sys.executable); data_dir = base_dir; ui_base = os.path.join(base_dir, 'ui'); doc_base = os.path.join(base_dir, 'doc'); locale_base = os.path.join(base_dir, 'locale'); plugin_base = os.path.join(base_dir)

icon_base = os.path.join(data_dir, 'icons')
