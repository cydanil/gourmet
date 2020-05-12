from tempfile import TemporaryDirectory
import traceback
import sys

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # noqa: import not a top of file

from gourmet import convert, gglobals  # noqa: import not at top
from gourmet.reccard import add_with_undo, RecCard, RecCardDisplay  # noqa


VERBOSE = True


def print_(*msg):
    if VERBOSE:
        print(*msg)


def assert_with_message(callable_, description):
    try:
        assert(callable_())
    except AssertionError:
        print('FAILED:', description)
        raise
    else:
        if VERBOSE:
            print('SUCCEEDED:', description)


def add_save_and_check(rc, lines_groups_and_dc):
    idx = rc.recipe_editor.module_tab_by_name["ingredients"]
    ing_controller = rc.recipe_editor.modules[idx].ingtree_ui.ingController

    # add_with_undo is what's called by any of the ways a user can add an ingredient.
    ing_editor = ing_controller.ingredient_editor_module
    added = []
    for line, group, desc in lines_groups_and_dc:
        add_with_undo(
            rc,
            lambda *args: added.append(ing_editor.add_ingredient_from_line(line, group_iter=group))
        )

    history = ing_editor.history
    print_("add_save_and_check UNDO HISTORY:", history)

    added = [ing_controller.get_persistent_ref_from_iter(i) for i in added]

    # Make a save via the callback, which would normally be called via the
    # Save button in the recipe editor window.
    rc.recipe_editor.save_cb()

    ings = rc.rd.get_ings(rc.current_rec)
    check_ings([i[2] for i in lines_groups_and_dc],ings)
    print_("add_save_and_check.return:", lines_groups_and_dc, "->", added)
    return added


def check_ings (check_dics,ings):
    """Given a list of dictionaries of properties to check and
    ingredients, check that our ingredients have those properties.  We
    assume our check_dics refer to the last ingredients in the list
    ings
    """
    n = -1
    check_dics.reverse()
    for dic in check_dics:
        ings[n]
        for k,v in list(dic.items()):
            try:
                assert(getattr(ings[n],k)==v)
            except AssertionError:
                #print 'Failed assertion',n,k,v,ings[n]
                #print 'We are looking for: '
                #for d in check_dics: print ' ',d
                #print 'in:'
                #for a,u,i in [(i.amount,i.unit,i.item) for i in ings]: print ' ',a,u,i
                #print 'we are at ',n,ings[n].amount,ings[n],ings[n].unit,ings[n].item
                #print 'we find ',k,'=',getattr(ings[n],k),'instead of ',v
                raise
        n -= 1


def test_ingredients_editing(rc):
    """In a recipe card, test ingredient editing"""
    # Show the ingredients tab
    rc.show_edit('ingredients')

    # Create an new ingredient group
    idx = rc.recipe_editor.module_tab_by_name["ingredients"]
    ing_controller = rc.recipe_editor.modules[idx].ingtree_ui.ingController
    i_group = ing_controller.add_group('Foo bar')

    print_("Testing ingredient editing - add 4 ingredients to a group.")
    add_save_and_check(
        rc,
        [['1 c. sugar', i_group,
         {'amount':1,'unit':'c.','item':'sugar','inggroup':'Foo bar'}],
        ['1 c. silly; chopped and sorted', i_group,
         {'amount':1,'unit':'c.','ingkey':'silly','inggroup':'Foo bar'}],
        ['1 lb. very silly', i_group,
         {'amount':1,'unit':'lb.','item':'very silly','inggroup':'Foo bar'}],
        ['1 tbs. extraordinarily silly', i_group,
         {'amount':1,'unit':'tbs.','item':'extraordinarily silly','inggroup':'Foo bar'}],
        ])
    print_("Ingredient editing successful")


def test_ingredients_undo(rc):
    """In a recipe card, test adding ingredients and undoing that"""
    # Show the ingredients tab
    rc.show_edit('ingredients')

    # Create a group with a single ingredient.
    # NB. adding more ingredients will require more undos
    ings_groups_and_dcs = [
        ['1 c. oil',None,{'amount':1,'unit':'c.','item':'oil'}]
    ]
    refs = add_save_and_check(rc, ings_groups_and_dcs)

    idx = rc.recipe_editor.module_tab_by_name["ingredients"]
    ing_controller = rc.recipe_editor.modules[idx].ingtree_ui.ingController
    del_iter = [ing_controller.get_iter_from_persisten_ref(r) for r in refs]
    print_(f"refs: {refs}")
    print_(f"-> {del_iter}")

    # Delete the ingredients from the recipe card
    ing_controller.delete_iters(*del_iter)
    print_(f"test_ing_undo - just deleted - UNDO HISTORY: {rc.history}")

    # Save the edits by calling the callback that normally would be executed
    # upon button press.
    rc.saveEditsCB()

    # Try to access the previously added ingredient.
    # If that raises an AssertionError, it means that the deletion
    # worked as expected.
    try:
        ii = rc.rd.get_ings(rc.current_rec)
        check_ings([i[2] for i in ings_groups_and_dcs], ii)
    except AssertionError:
        print_('Deletion worked!')
    else:
        print_([i[2] for i in ings_groups_and_dcs])
        print_('corresponds to')
        print_([(i.amount,i.unit,i.item) for i in ii])
        raise Exception("Ingredients Not Deleted!")

    # The meat of the test is to undo the deletion
    # Undo the deletion and save the card. The content should now be
    # what it was at the beginning.
    rc.undo.emit('activate')
    print_(f"test_ing_undo - pressed undo - history: {rc.history}")
    rc.saveEditsCB()

    # Check that our ingredients have been put back properly by the undo action
    print_('Checking for ',[i[2] for i in ings_groups_and_dcs])
    print_('Checking in ',rc.rd.get_ings(rc.current_rec))
    check_ings([i[2] for i in ings_groups_and_dcs],
                rc.rd.get_ings(rc.current_rec))
    print_('Undo deletion worked!')


def test_ingredients_group_editing(rc):
    # Show the ingredients tab
    rc.show_edit('ingredients')

    idx = rc.recipe_editor.module_tab_by_name["ingredients"]
    ing_controller = rc.recipe_editor.modules[idx].ingtree_ui.ingController

    # The test relies on the first item being a group
    itr = ing_controller.imodel.get_iter(0,)
    rc.ingtree_ui.change_group(itr,'New Foo')
    rc.saveEditsCB()
    ings = rc.rd.get_ings(rc.current_rec)
    assert(ings[0].inggroup == 'New Foo') # Make sure our new group got saved
    print_('Group successfully changed to "New Foo"')
    rc.undo.emit('activate') # Undo
    assert(rc.save.get_sensitive()) # Make sure "Save" is sensitive after undo
    rc.saveEditsCB() # Save new changes
    ings = rc.rd.get_ings(rc.current_rec)
    assert(ings[0].inggroup != 'New Foo') # Make sure our new group got un-done
    print_('Undo of group change worked.')


def test_undo_save_sensitivity(rc):
    # Show the description tab
    rc.show_edit('description')

    # Make a save via the callback, which would normally be called via the
    # Save button in the recipe editor window.
    rc.recipe_editor.save_cb()

    # Check that the `save` and `revert` push buttons are disabled.
    action = rc.recipe_editor.mainRecEditActionGroup.get_action('Save')
    is_enabled = action.get_sensitive()
    assert not is_enabled, "Save Button not de-sensitized after save"

    action = rc.recipe_editor.mainRecEditActionGroup.get_action('Revert')
    is_enabled = action.get_sensitive()
    assert not is_enabled, "Revert Button not de-sensitized after save"

    test_values = {'preptime': 30 * 60, 'cooktime': 60 * 60, 'title': 'Foo bar',
                   'cuisine': 'Mexican', 'category': 'Entree', 'rating': 8}

    card_display = RecCardDisplay(rc, rc.rg, rc.current_rec)
    for wname, value in test_values.items():
        # Get the widget from the RecCardDisplay
        widget = getattr(card_display, f"{wname}Display")
        print_(f"TESTING {wname}")

        if isinstance(value, int):
            value = convert.seconds_to_timestring(value)

        if wname in card_display.special_display_functions:
            orig_value = widget.get_active_text()
            widget.set_text(value)
            get_method = widget.get_active_text
            print_(f"Set with entry.set_value({value})")
        else:
            orig_value = widget.get_text()
            widget.set_text(value)
            get_method = widget.get_text
            print_(f"Set with set_text({value})")

        msg = f"{wname} not set correctly: {get_method()}, should be {value}"
        assert get_method() == value, msg

        action = rc.recipe_editor.mainRecEditActionGroup.get_action('Save')
        is_enabled = action.get_sensitive()
        assert not is_enabled, "Save button not de-sensitized after save"

        action = rc.recipe_editor.mainRecEditActionGroup.get_action('Revert')
        is_enabled = action.get_sensitive()
        assert not is_enabled, "Revert button not de-sensitized after save"
        print_('-- Hitting Revert')
        # Make a revert via the callback, which would normally be done via the
        # Revert button in the recipe editor window.
        rc.recipe_editor.revert_cb()

        assert_with_message(
            lambda : get_method()==orig_value,
            'Value of %s set to %s after Undo'%(widget,orig_value)
            )
        assert_with_message(
            lambda: not rc.save.get_sensitive(),
            'Save desensitized correctly after unsetting %s'%widget
            )
        print_("-- Hitting 'REDO'")
        rc.redo.emit('activate')
        if orig_value and type(value)!=int:
            print_("(Hitting redo a second time for text...)")
            rc.redo.emit('activate') # Blank text, then fill it
        assert_with_message(
            lambda : get_method()==value,
            'Value of %s set to %s (should be %s)'%(widget,
                                                          get_method(),
                                                          value)
            )
        assert_with_message(rc.save.get_sensitive,
                            'Save sensitized after setting %s via REDO'%widget)
        print_('-- Hitting UNDO again')
        rc.undo.emit('activate')
        if orig_value and type(value)!=int:
            print_('(Hitting UNDO a second time for text)')
            rc.undo.emit('activate') # Blank text, then fill it
        assert_with_message(
            lambda : get_method()==orig_value,
            'Value unset properly on for %s UNDO->REDO->UNDO'%widget
            )
        try:
            assert_with_message(lambda : not rc.save.get_sensitive(),
                                'Save desensitized after undo->redo->undo of %s'%widget)
        except:
            print('rc.widgets_changed_since_save',rc.widgets_changed_since_save)
            raise
        print_('DONE TESTING %s'%widget)

# {'description': 0, 'ingredients': 1, 'instructions': 2, 'notes': 3}


with TemporaryDirectory(prefix='gourmet_', suffix='_test_reccard') as tmpdir:
    gglobals.gourmetdir = tmpdir
    rec_card = RecCard()

    try:
        test_ingredients_editing(rec_card)
        print('Ing Editing works!')
        # test_ingredients_undo(rec_card)
        print('Ing Undo works!')
        test_undo_save_sensitivity(rec_card)
        print('Undo properly sensitizes save widget.')
        test_ingredients_group_editing(rec_card)
        print('Ing Group Editing works.')
    except AssertionError:
        traceback.print_exc()
        Gtk.main()
    else:
        rec_card.hide()
        sys.exit()
