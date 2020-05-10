from tempfile import TemporaryDirectory
import traceback
import sys

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # noqa: import not a top of file

from gourmet import gglobals  # noqa: import not at top
from gourmet.reccard import add_with_undo, RecCard  # noqa: import not at top


VERBOSE = True


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
    added = []
    for l, g, dc in lines_groups_and_dc:
        # add_with_undo is what's called by any of the ways a user can add an ingredient.
        add_with_undo(
            rc,
            lambda *args: added.append(rc.add_ingredient_from_line(l,group_iter=g))
            )
    #print 'add_save_and_check UNDO HISTORY:',rc.history
    added = [rc.ingtree_ui.ingController.get_persistent_ref_from_iter(i) for i in added]
    rc.saveEditsCB()
    ings = rc.rd.get_ings(rc.current_rec)
    check_ings([i[2] for i in lines_groups_and_dc],ings)
    #print 'add_save_and_check.return:',lines_groups_and_dc,'->',added
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


def test_ing_editing(rc):
    """In a recipe card, test ingredient editing"""
    # Show the ingredients tab
    rc.show_edit('ingredients')

    # Create an new ingredient group
    i_controller = rc.recipe_editor.modules[1].ingtree_ui.ingController
    i_group = i_controller.add_group('Foo bar')

    if VERBOSE:
        print("Testing ingredient editing - add 4 ingredients to a group.")
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
    if VERBOSE:
        print("Ingredient editing successful")


def test_ing_undo(rc):
    """In a recipe card, test adding ingredients and undoing that"""
    # Show the ingredients tab
    rc.show_edit('ingredients')

    # Create a group with a single ingredient.
    # NB. adding more ingredients will require more undos
    ings_groups_and_dcs = [
        ['1 c. oil',None,{'amount':1,'unit':'c.','item':'oil'}]
    ]
    refs = add_save_and_check(rc, ings_groups_and_dcs)

    i_controller = rc.recipe_editor.modules[1].ingtree_ui.ingController
    del_iter = [i_controller.get_iter_from_persisten_ref(r) for r in refs]
    if VERBOSE:
        print(f"refs: {refs}")
        print(f"-> {del_iter}")

    # Delete the ingredients from the recipe card
    i_controller.delete_iters(*del_iter)
    if VERBOSE:
        print(f"test_ing_undo - just deleted - UNDO HISTORY: {rc.history}")

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
        if VERBOSE:
            print('Deletion worked!')
    else:
        if VERBOSE:
            print([i[2] for i in ings_groups_and_dcs])
            print('corresponds to')
            print([(i.amount,i.unit,i.item) for i in ii])
        raise Exception("Ingredients Not Deleted!")

    # The meat of the test is to undo the deletion
    # Undo the deletion and save the card. The content should now be
    # what it was at the beginning.
    rc.undo.emit('activate')
    if VERBOSE:
        print(f"test_ing_undo - pressed undo - history: {rc.history}")
    rc.saveEditsCB()

    # Check that our ingredients have been put back properly by the undo action
    if VERBOSE:
        print('Checking for ',[i[2] for i in ings_groups_and_dcs])
        print('Checking in ',rc.rd.get_ings(rc.current_rec))
    check_ings([i[2] for i in ings_groups_and_dcs],
                rc.rd.get_ings(rc.current_rec))
    if VERBOSE:
        print('Undo deletion worked!')


def test_ing_group_editing(rc):
    # Show the ingredients tab
    rc.show_edit('ingredients')

    # TODO: check module index correct
    i_controller = rc.recipe_editor.modules[1].ingtree_ui.ingController

    # The test relies on the first item being a group
    itr = i_controller.imodel.get_iter(0,)
    rc.ingtree_ui.change_group(itr,'New Foo')
    rc.saveEditsCB()
    ings = rc.rd.get_ings(rc.current_rec)
    assert(ings[0].inggroup == 'New Foo') # Make sure our new group got saved
    if VERBOSE: print('Group successfully changed to "New Foo"')
    rc.undo.emit('activate') # Undo
    assert(rc.save.get_sensitive()) # Make sure "Save" is sensitive after undo
    rc.saveEditsCB() # Save new changes
    ings = rc.rd.get_ings(rc.current_rec)
    assert(ings[0].inggroup != 'New Foo') # Make sure our new group got un-done
    if VERBOSE: print('Undo of group change worked.')


def test_undo_save_sensitivity(rc):
    # Show the description tab
    rc.show_edit('description')

    rc.saveEditsCB()
    assert_with_message(
        lambda : not rc.save.get_sensitive(),
        'SAVE Button not properly desensitized after save'
        )
    for widget,value in [
                         ('preptime',30*60),
                         ('cooktime',60*60),
                         ('title','Foo bar'),
                         ('cuisine','Mexican'),
                         ('category','Entree'),
                         ('rating',8),
                         ]:
        if VERBOSE: print('TESTING ',widget)
        if type(value)==int:
            orig_value = rc.rw[widget].get_value()
            rc.rw[widget].set_value(value)
            get_method = rc.rw[widget].get_value
            if VERBOSE: print('Set with set_value(',value,')')
        elif widget in rc.reccom:
            orig_value = rc.rw[widget].entry.get_text()
            rc.rw[widget].entry.set_text(value)
            get_method = rc.rw[widget].entry.get_text
            if VERBOSE: print('Set with entry.set_text(',value,')')
        else:
            orig_value = rc.rw[widget].get_text()
            rc.rw[widget].set_text(value)
            get_method = rc.rw[widget].get_text
            if VERBOSE: print('Set with set_text(',value,')')
        assert_with_message(
            lambda : get_method()==value,
            '''Value set properly for %s to %s (should be %s)'''%(
            widget,get_method(),value
            )
            )
        assert_with_message(rc.save.get_sensitive,
                            'Save sensitized after setting %s'%widget)
        assert_with_message(rc.undo.get_sensitive,
                            'Undo sensitized after setting %s'%widget)
        print('-- Hitting UNDO')
        rc.undo.emit('activate')
        while Gtk.events_pending():
            Gtk.main_iteration()
        if orig_value and type(value)!=int: rc.undo.emit('activate') # Blank text, then fill it
        assert_with_message(
            lambda : get_method()==orig_value,
            'Value of %s set to %s after Undo'%(widget,orig_value)
            )
        assert_with_message(
            lambda: not rc.save.get_sensitive(),
            'Save desensitized correctly after unsetting %s'%widget
            )
        if VERBOSE: print("-- Hitting 'REDO'")
        rc.redo.emit('activate')
        if orig_value and type(value)!=int:
            if VERBOSE: print("(Hitting redo a second time for text...)")
            rc.redo.emit('activate') # Blank text, then fill it
        assert_with_message(
            lambda : get_method()==value,
            'Value of %s set to %s (should be %s)'%(widget,
                                                          get_method(),
                                                          value)
            )
        assert_with_message(rc.save.get_sensitive,
                            'Save sensitized after setting %s via REDO'%widget)
        print('-- Hitting UNDO again')
        rc.undo.emit('activate')
        if orig_value and type(value)!=int:
            if VERBOSE: print('(Hitting UNDO a second time for text)')
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
        if VERBOSE: print('DONE TESTING %s'%widget)

# {'description': 0, 'ingredients': 1, 'instructions': 2, 'notes': 3}


with TemporaryDirectory(prefix='gourmet_', suffix='_test_reccard') as tmpdir:
    gglobals.gourmetdir = tmpdir
    rec_card = RecCard()

    try:
        # test_ing_editing(rec_card)
        print('Ing Editing works!')
        # test_ing_undo(rec_card)
        print('Ing Undo works!')
        test_undo_save_sensitivity(rec_card)
        print('Undo properly sensitizes save widget.')
        test_ing_group_editing(rec_card)
        print('Ing Group Editing works.')
    except AssertionError:
        traceback.print_exc()
        Gtk.main()
    else:
        rec_card.hide()
        sys.exit()
