from pathlib import Path

from dogtail.procedural import click, focus, keyCombo
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
    focus.table()
    keyCombo("<Up>")

    # Open it, and its recipe editor, to add ingredients
    keyCombo("<Ctrl>o")
    click("Edit ingredients")

    # Focus on the recipe editor and add a new ingredient
    focus.window("Fancy Recipe (Edit)")
    focus.text()
    type("1 cup flour")
    keyCombo("<Enter>")

    # Close the window and cancel when asked to save changes
    keyCombo("<Alt><F4>")
    click("Cancel")

    # Assert that the recipe editor is still open
    focus.window("Fancy Recipe (Edit)")

    # Close the window using a different shortcut
    keyCombo("<Ctrl>W")
    # Use a shortcut to validate saving, as dogtail does not find the button :/
    keyCombo("<Alt>S")

    # There are now two windows, the recipe card, and main window
    # Close them successively to quit the application
    keyCombo("<Alt><F4>")
    keyCombo("<Alt><F4>")


if __name__ == "__main__":
    test_cancel_edit_in_recipe_editor()
