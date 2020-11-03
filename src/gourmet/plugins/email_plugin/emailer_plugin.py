import webbrowser
from gettext import gettext as _
from typing import List

from gi.repository import Gtk

from gourmet.backends.db import RecData
from gourmet.convert import seconds_to_timestring
from gourmet.gtk_extras.dialog_extras import getBoolean
from gourmet.plugin import MainPlugin, UIPlugin


class EmailRecipePlugin(MainPlugin, UIPlugin):

    ui_string = """
   <menubar name="RecipeIndexMenuBar">
         <menu name="Tools" action="Tools">
       <placeholder name="StandaloneTool">
           <menuitem action="EmailRecipes"/>
       </placeholder>
   </menu>
   </menubar>"""

    def setup_action_groups(self):
        self.actionGroup = Gtk.ActionGroup(name='RecipeEmailerActionGroup')
        self.actionGroup.add_actions([
            ('EmailRecipes', None, _('Email recipes'),
             None, _('Email all selected recipes (or all recipes if no recipes are selected'),  # noqa
             self.email_selected)])
        self.action_groups.append(self.actionGroup)

    def activate(self, pluggable):
        self.rg = self.pluggable = pluggable
        self.add_to_uimanager(pluggable.ui_manager)

    def email_selected(self, *args):
        recipes = self.rg.get_selected_recs_from_rec_tree()

        if not recipes:  # no recipe were selected
            return

        if len(recipes) > 20:
            if not getBoolean(title=_('Email recipes'),
                              sublabel=_('Do you really want to email all %s selected recipes?') % l,  # noqa
                              custom_yes=_('Yes, e_mail them'),
                              cancel=False):
                return

        mailto_link = self.format_recipes(recipes)
        webbrowser.open(mailto_link)

    @staticmethod
    def join_ingredients(ingredients: List) -> str:
        template = r'{amount} {unit} {item}'
        ret = ''
        for ingredient in ingredients:
            ret += template.format(amount=ingredient.amount,
                                   unit=ingredient.unit,
                                   item=ingredient.item)
            ret += '\n'
        return ret

    @staticmethod
    def format_recipes(recipes: List[str]) -> str:
        link = r"mailto://?subject={subject}&body={body}"
        template = r"""
# {title}

rating: {rating}
preparation time: {preptime}
cooking time: {cooktime}
makes: {yields} {yield_unit}
source: {source}

## Ingredients
{ingredients}

## Instructions
{instructions}
"""
        db = RecData.instance_for()
        if len(recipes) == 1:
            subject = recipes[0].title
        else:
            subject = "Gourmet Recipes"

        body = ""
        for recipe in recipes:
            ingredients = db.get_ings(recipe.id)
            ingredients = EmailRecipePlugin.join_ingredients(ingredients)
            source = recipe.source if recipe.source else recipe.link
            preptime = seconds_to_timestring(recipe.preptime)
            cooktime = seconds_to_timestring(recipe.cooktime)

            body += template.format(title=recipe.title,
                                    rating=recipe.rating,
                                    preptime=preptime,
                                    cooktime=cooktime,
                                    yields=recipe.yields,
                                    yield_unit=recipe.yield_unit,
                                    ingredients=ingredients,
                                    instructions=recipe.instructions,
                                    source=source)
            body += "\n"
        return link.format(subject=subject, body=body)
