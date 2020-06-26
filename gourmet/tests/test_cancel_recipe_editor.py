from pathlib import Path
import sys

from dogtail import procedural
from dogtail import tree
from dogtail.utils import run


def test_cancel_edit_in_recipe_editor():
    """Dogtail integration test: recipe editor behaves as intended on saves."""

    dbpath = Path(__file__).parent / 'old_databases' / 'current' / 'recipes.db'
    cmd = f"gourmet --database-url sqlite:///{dbpath}"

    pid = run(cmd, timeout=3)
    gourmet = None

    for app in tree.root.applications():
        if app.get_process_id() == pid:
            gourmet = app
            break

    assert gourmet is not None, "Could not find Gourmet instance!"

    # Get the first recipe in the list
    procedural.focus.table()
    procedural.keyCombo("<Up>")

    # Open it, and its recipe editor, to add ingredients
    procedural.keyCombo("<Ctrl>o")
    procedural.click("Edit ingredients")

    # Focus on the recipe editor and add a new ingredient
    procedural.focus.window("Fancy Recipe (Edit)")
    procedural.focus.text()
    procedural.type("1 cup flour")
    procedural.keyCombo("<Enter>")

    # Close the window and cancel when asked to save changes
    procedural.keyCombo("<Alt><F4>")
    procedural.click("Cancel")

    # Assert that the recipe editor is still open
    procedural.focus.window("Fancy Recipe (Edit)")

    # Close the window using a different shortcut
    procedural.keyCombo("<Ctrl>W")
    # Use a shortcut to validate saving, as dogtail does not find the button :/
    procedural.keyCombo("<Alt>S")

    # There are now two windows, the recipe card, and main window
    # Close them successively to quit the application
    procedural.keyCombo("<Alt><F4>")
    procedural.keyCombo("<Alt><F4>")


if __name__ == "__main__":
    test_cancel_edit_in_recipe_editor()
