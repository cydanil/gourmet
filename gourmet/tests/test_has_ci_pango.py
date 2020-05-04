import gi
gi.require_versions({'Gtk': '3.0', 'Pango': '1.0'})
from gi.repository import Pango  # noqa

assert hasattr(Pango.AttrList, 'get_iterator')
