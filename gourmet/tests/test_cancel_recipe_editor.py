from pathlib import Path
import warnings

from dogtail import procedural
from dogtail import tree
from dogtail.utils import run


def test_cancel_edit_in_recipe_editor():
    warnings.filterwarnings("error")

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

    # Close the application like savages


if __name__ == "__main__":
    test_cancel_edit_in_recipe_editor()
