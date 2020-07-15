# -*- coding: utf-8 -*-
#
## we set up default information.

## first, easy to maintain lists which can eventually be moved to
## files.

from .abstractLang import AbstractLanguage
from typing import List, Mapping

class Language(AbstractLanguage):

    # TRANSLATOR WARNING: DO NOT TRANSLATE THE FIELD NAMES: ONLY THE VALUES!!!
    fields={'cuisine': ['English','Scottish','Welsh','Irish','American',
                        'Italian','French','Mexican','Indian',
                        'Southwestern','Asian/Thai','Asian/Vietnamese',
                        'Asian/Chinese','Asian/Japanese',],
            'rating' : ['Excellent','Great','Good','Fair','Poor'],
            'source' : [],
            'category' : ['Dessert','Entree','Salad','Soup',
                          'Breakfast'],
                      }

    SYNONYMS=[
        # the first item of each list is the
        ["aubergine","eggplant"],
        ["azuki beans", "adzuki beans", "adzuki", "azuki"],
        ["beet","beetroot"],
        ["capsicum","chilli pepper"],
        ["chinese gooseberry","kiwi fruit","kiwi"],
        ["chinese leaves","bok choy"],
        ["chokeberry","cooking apple"],
        ["coriander","cilantro"],
        ["courgette","zucchini"],
        ["dragonfruit" , "pitaya"],
        ["green pepper", "bell pepper","green bell pepper", "pepper"],
        ["jackfruit","nangka"],
        ["juneberry","saskatoon"],
        ["langsat","longkong", "duku"],
        ["maise","sweetcorn","corn","sweet corn"],
        ["mamoncillo", "quenepa", "genip"],
        ["mangetout","snap peas"],
        ["nannyberry","sheepberry"],
        ["red bell pepper","red pepper"],
        ["rocket","arugula"],
        ["rose apple", "malay apple"],
        ["salak", "snakefruit"],
        ["sapodilla", "chiku", "sapadilla", "snake fruit", "sawo"],
        ["soursop", "guanabana"],
        ["spring greens","collard greens"],
        ["spring onion","scallion","green onion"],
        ["start fruit","carambola"],
        ["sunberry","wonderberry"],
        ["swede","rutubaga"],
        ["velvet persimmon","mabolo"],
        ["black cod","sablefish"],
        ["patagonian toothfish","chilean sea bass"],
        ]

    # a dictionary key=ambiguous word, value=list of terms
    AMBIGUOUS: Mapping[str, List[str]] = {}


    # triplicates ITEM, KEY, SHOPPING CATEGORY
    INGREDIENT_DATA = [("alfalfa sprouts","alfalfa sprouts","produce"),
                       ("anise","anise","produce"),
                       ("artichoke","artichoke","produce"),
                       ("arugula","arugula","produce"),
                       ("asparagus","asparagus","produce"),
                       ("aubergine","aubergine","produce"),
                       ("avocado","avocado","produce"),
                       ("green beans","green beans","produce"),
                       ("azuki beans","azuki beans","produce"),
                       ("bean sprouts","bean sprouts","produce"),
                       ("black beans","black beans","produce"),
                       ("black-eyed peas","black-eyed peas","produce"),
                       ("borlotti beans","borlotti beans","produce"),
                       ("broad beans","broad beans","produce"),
                       ("chickpeas, garbanzos, or ceci beans","chickpeas, garbanzos, or ceci beans","produce"),
                       ("green beans","green beans","produce"),
                       ("kidney beans","kidney beans","produce"),
                       ("lentils","lentils","produce"),
                       ("lima bean or butter bean","lima bean or butter bean","produce"),
                       ("mung beans","mung beans","produce"),
                       ("navy beans","navy beans","produce"),
                       ("runner beans","runner beans","produce"),
                       ("soybeans","soybeans","produce"),
                       ("peas","peas","produce"),
                       ("snap peas","snap peas","produce"),
                       ("bok choy","bok choy","produce"),
                       ("breadfruit","breadfruit","produce"),
                       ("broccoflower","broccoflower","produce"),
                       ("broccoli","broccoli","produce"),
                       ("brussels sprouts","brussels sprouts","produce"),
                       ("cabbage","cabbage","produce"),
                       ("calabrese","calabrese","produce"),
                       ("cauliflower","cauliflower","produce"),
                       ("celery","celery","produce"),
                       ("chard","chard","produce"),
                       ("cilantro","cilantro","produce"),
                       ("collard greens","collard greens","produce"),
                       ("corn salad","corn salad","produce"),
                       ("endive","endive","produce"),
                       ("fennel","fennel","produce"),
                       ("fiddleheads","fiddleheads","produce"),
                       ("frisee","frisee","produce"),
                       ("kale","kale","produce"),
                       ("kohlrabi","kohlrabi","produce"),
                       ("lemon grass","lemon grass","produce"),
                       ("lettuce lactuca sativa","lettuce lactuca sativa","produce"),
                       ("corn","corn","produce"),
                       ("mushrooms","mushrooms","produce"),
                       ("mustard greens","mustard greens","produce"),
                       ("nettles","nettles","produce"),
                       ("new zealand spinach","new zealand spinach","produce"),
                       ("okra","okra","produce"),
                       ("onion family","onion family","produce"),
                       ("chives","chives","produce"),
                       ("garlic","garlic","produce"),
                       ("leek allium porrum","leek allium porrum","produce"),
                       ("onion","onion","produce"),
                       ("shallot","shallot","produce"),
                       ("scallion","scallion","produce"),
                       ("parsley","parsley","produce"),
                       ("pepper","pepper","produce"),
                       ("red bell pepper","red bell pepper","produce"),
                       ("chilli pepper","chilli pepper","produce"),
                       ("jalapeño pepper","pepper, jalapeño","produce"),
                       ("habanero pepper","pepper, habanero","produce"),
                       ("radicchio","radicchio","produce"),
                       ("rapini","rapini","produce"),
                       ("rhubarb","rhubarb","produce"),
                       ("root vegetables","root vegetables","produce"),
                       ("beet","beet","produce"),
                       ("carrot","carrot","produce"),
                       ("cassava (manioc)","cassava (manioc)","produce"),
                       ("celeriac","celeriac","produce"),
                       ("daikon","daikon","produce"),
                       ("fennel","fennel","produce"),
                       ("ginger","ginger","produce"),
                       ("parsnip","parsnip","produce"),
                       ("radish","radish","produce"),
                       ("rutabaga","rutabaga","produce"),
                       ("turnip","turnip","produce"),
                       ("wasabi","wasabi","produce"),
                       ("white radish","white radish","produce"),
                       ("skirret","skirret","produce"),
                       ("spinach","spinach","produce"),
                       ("acorn squash","squash, acorn","produce"),
                       ("butternut squash","squash, butternut","produce"),
                       ("courgette","courgette","produce"),
                       ("cucumber","cucumber","produce"),
                       ("gem squash","squash, gem","produce"),
                       ("patty pans","patty pans","produce"),
                       ("pumpkin","pumpkin","produce"),
                       ("spaghetti squash","squash, spaghetti","produce"),
                       ("tat soi","tat soi","produce"),
                       ("tomato","tomato","produce"),
                       ("jicama","jicama","produce"),
                       ("jerusalem artichoke","jerusalem artichoke","produce"),
                       ("potato","potato","produce"),
                       ("sweet potato","sweet potato","produce"),
                       ("taro","taro","produce"),
                       ("yam","yam","produce"),
                       ("water chestnut","water chestnut","produce"),
                       ("watercress","watercress","produce"),
                       # fruits, from wikipedia list
                       ("apple","apple","produce"),
                       ("green apple","green apple","produce"),
                       ("crabapple","crabapple","produce"),
                       ("chokeberry","chokeberry","produce"),
                       ("hawthorn","hawthorn","produce"),
                       ("juneberry","juneberry","produce"),
                       ("loquat","loquat","produce"),
                       ("medlar","medlar","produce"),
                       ("pomegranate","pomegranate","produce"),
                       ("quince","quince","produce"),
                       ("rowan","rowan","produce"),
                       ("rose hip","rose hip","produce"),
                       ("apricot","apricot","produce"),
                       ("cherry","cherry","produce"),
                       ("plum","plum","produce"),
                       ("peach","peach","produce"),
                       ("nectarine","nectarine","produce"),
                       ("blackberry","blackberry","produce"),
                       ("boysenberry","boysenberry","produce"),
                       ("raspberry","raspberry","produce"),
                       ("cloudberry","cloudberry","produce"),
                       ("wineberry","wineberry","produce"),
                       ("bearberry","bearberry","produce"),
                       ("bilberry","bilberry","produce"),
                       ("blueberry ","blueberry ","produce"),
                       ("cranberry ","cranberry ","produce"),
                       ("huckleberry ","huckleberry ","produce"),
                       ("lingonberry","lingonberry","produce"),
                       ("barberry ","barberry ","produce"),
                       ("red currant","currant, red","produce"),
                       ("black currant","currant, black","produce"),
                       ("white currant","currant, white","produce"),
                       ("elderberry ","elderberry ","produce"),
                       ("gooseberry ","gooseberry ","produce"),
                       ("nannyberry","nannyberry","produce"),
                       ("sea-buckthorn","sea-buckthorn","produce"),
                       ("wolfberry","wolfberry","produce"),
                       ("crowberry","crowberry","produce"),
                       ("mulberry","mulberry","produce"),
                       ("goumi","goumi","produce"),
                       ("kiwi fruit ","kiwi fruit ","produce"),
                       ("persimmon ","persimmon ","produce"),
                       ("buffaloberry","buffaloberry","produce"),
                       ("pawpaw","pawpaw","produce"),
                       ("american persimmon","american persimmon","produce"),
                       ("prickly pear ","prickly pear ","produce"),
                       ("saguaro","saguaro ","produce"),
                       ("pitaya","pitaya","produce"),
                       ("cantaloupe","cantaloupe","produce"),
                       ("honeydew","honeydew","produce"),
                       ("sunberry","sunberry","produce"),
                       ("watermelon ","watermelon ","produce"),
                       ("strawberry ","strawberry ","produce"),
                       ("angelica","angelica","produce"),
                       ("rhubarb","rhubarb","produce"),
                       ("fig ","fig ","produce"),
                       ("grape","grape","produce"),
                       ("jujube","jujube","produce"),
                       ("black mulberry","black mulberry","produce"),
                       ("pomegranate","pomegranate","produce"),
                       ("date","date","produce"),
                       ("citron","citron","produce"),
                       ("grapefruit","grapefruit","produce"),
                       ("pommelo","pommelo","produce"),
                       ("key lime","key lime","produce"),
                       ("kumquat","kumquat","produce"),
                       ("lemon","lemon","produce"),
                       ("lime","lime","produce"),
                       ("mandarin","mandarin","produce"),
                       ("clementine","clementine","produce"),
                       ("tangelo","tangelo","produce"),
                       ("tangerine","tangerine","produce"),
                       ("orange","orange","produce"),
                       ("ugli fruit","ugli fruit","produce"),
                       ("guava ","guava ","produce"),
                       ("longan","longan","produce"),
                       ("lychee","lychee","produce"),
                       ("passion fruit","passion fruit","produce"),
                       ("feijoa","feijoa","produce"),
                       ("akee","akee","produce"),
                       ("banana","banana","produce"),
                       ("plantain","plantain","produce"),
                       ("breadfruit","breadfruit","produce"),
                       ("camucamu","camucamu","produce"),
                       ("star fruit","star fruit","produce"),
                       ("cempedak","cempedak","produce"),
                       ("cherimoya","cherimoya","produce"),
                       ("coconut","coconut","produce"),
                       ("custard apple","custard apple","produce"),
                       ("dragonfruit","dragonfruit","produce"),
                       ("durian","durian","produce"),
                       ("guarana","guarana","produce"),
                       ("jackfruit","jackfruit","produce"),
                       ("keppel fruit","keppel fruit","produce"),
                       ("langsat","langsat","produce"),
                       ("velvet persimmon","velvet persimmon","produce"),
                       ("mamey sapote","mamey sapote","produce"),
                       ("mamoncillo","mamoncillo","produce"),
                       ("mango","mango","produce"),
                       ("mangosteen","mangosteen","produce"),
                       ("marang","marang","produce"),
                       ("papaya","papaya","produce"),
                       ("peanut butter fruit","peanut butter fruit","produce"),
                       ("pineapple","pineapple","produce"),
                       ("poha","poha","produce"),
                       ("rambutan","rambutan","produce"),
                       ("rose apple","rose apple","produce"),
                       ("salak","salak","produce"),
                       ("sapodilla","sapodilla","produce"),
                       ("soursop","soursop","produce"),
                       ("sugar apple","sugar apple","produce"),
                       ("tamarind","tamarind","produce"),
                       ## seafood, from wikipedia list
                       ("anchovy","anchovy","seafood"),
                       ("bass","bass","seafood"),
                       ("striped bass","striped bass","seafood"),
                       ("black cod","black cod","seafood"),
                       ("blowfish","blowfish","seafood"),
                       ("catfish","catfish","seafood"),
                       ("cod","cod","seafood"),
                       ("eel","eel","seafood"),
                       ("flounder","flounder","seafood"),
                       ("haddock","haddock","seafood"),
                       ("halibut","halibut","seafood"),
                       ("lingcod","lingcod","seafood"),
                       ("mahi mahi","mahi mahi","seafood"),
                       ("monkfish","monkfish","seafood"),
                       ("orange roughy","orange roughy","seafood"),
                       ("chilean sea bass","chilean sea bass","seafood"),
                       ("pike","pike","seafood"),
                       ("pollock","pollock","seafood"),
                       ("sanddab","sanddab","seafood"),
                       ("sardine","sardine","seafood"),
                       ("salmon","salmon","seafood"),
                       ("sea bass","sea bass","seafood"),
                       ("shark","shark","seafood"),
                       ("snapper","snapper","seafood"),
                       ("rockfish","rockfish","seafood"),
                       ("rock cod","rock cod","seafood"),
                       ("pacific snapper","pacific snapper","seafood"),
                       ("red snapper","red snapper","seafood"),
                       ("sole","sole","seafood"),
                       ("sturgeon","sturgeon","seafood"),
                       ("surimi","surimi","seafood"),
                       ("swordfish","swordfish","seafood"),
                       ("tilapia","tilapia","seafood"),
                       ("tilefish","tilefish","seafood"),
                       ("trout","trout","seafood"),
                       ("tuna","tuna","seafood"),
                       ("whitefish","whitefish","seafood"),
                       ("whiting","whiting","seafood"),
                       ("roe","roe","seafood"),
                       ("caviar","caviar","seafood"),
                       ("salmon roe","salmon roe","seafood"),
                       ("crab","crab","seafood"),
                       ("dungness crab","dungness crab","seafood"),
                       ("king crab","king crab","seafood"),
                       ("snow crab","snow crab","seafood"),
                       ("crayfish","crayfish","seafood"),
                       ("lobster","lobster","seafood"),
                       ("shrimp","shrimp","seafood"),
                       ("prawns","prawns","seafood"),
                       ("abalone","abalone","seafood"),
                       ("clam","clam","seafood"),
                       ("mussel","mussel","seafood"),
                       ("octopus","octopus","seafood"),
                       ("oyster","oyster","seafood"),
                       ("snail","snail","seafood"),
                       ("squid","squid","seafood"),
                       ("scallop","scallop","seafood"),
                       ## meats (garnered from wikipedia lists)
                       ("bacon","bacon","meats"),
                       ("chorizo","chorizo","meats"),
                       ("fuet","fuet","meats"),
                       ("salami","salami","meats"),
                       ("ham","ham","meats"),
                       ("mutton","mutton","meats"),
                       ("lamb","lamb","meats"),
                       ("veal","veal","meats"),
                       ("steak","steak","meats"),
                       ("hamburger","hamburger","meats"),
                       ("roast beef","roast beef","meats"),
                       ("chicken","chicken","meats"),
                       ("turkey","turkey","meats"),
                       ("duck","duck","meats"),
                       ("goose","goose","meats"),
                       ## my old list
                       ("tamarind water","tamarind water", "international"),
                       ("tamarind juice","tamarind juice", "international"),
                       ('vegetable broth','broth, vegetable', 'soups&sauces'),
                       ('fresh basil','basil, fresh', 'produce',),
                       ('light sugar brown','sugar, light brown', 'baking',),
                       ('balsamic vinegar','vinegar, balsamic', 'wines&oils',),
                       ('zuchini','zuchini', 'produce',),
                       ('avocado','avocado', 'produce',),
                       ('walnut','walnut', 'baking',),
                       ('celery','celery', 'produce',),
                       ('coriander seeds','coriander, seeds', 'spices',),
                       ('provolone cheese','cheese, provolone', 'dairy',),
                       ('galanga','galanga', 'produce',),
                       ('couscous','couscous', 'pastas',),
                       ('rice','rice', 'pastas',),
                       ('flour tortillas','tortillas, flour', 'dairy',),
                       ('olive oil','oil, olive', 'wines&oils',),
                       ('vanilla extract','vanilla extract', 'baking',),
                       ('red potato-skinned','potato, red-skinned', 'produce',),
                       ('powdered ginger','ginger, powdered', 'spices',),
                       ('roasted chili paste','roasted chili paste', 'international',),
                       ('curry powder','curry powder', 'spices',),
                       ('dried shrimp','shrimp, dried', 'international',),
                       ('dijon mustard','mustard, dijon', 'condiments',),
                       ('whole rock cod or snapper','whole rock cod or snapper', 'seafood',),
                       ('shells pasta','pasta, shells', 'pastas',),
                       ('green canned chiles','green chiles, canned', 'international',),
                       ('nutmeg','nutmeg', 'spices',),
                       ('sourdough bread','bread, sourdough', 'bread',),
                       ('corn oil','oil, corn', 'wines&oils',),
                       ('lemon grass','lemon grass', 'produce',),
                       ('feta cheese','cheese, feta', 'dairy',),
                       ('jack cheese','cheese, jack', 'dairy',),
                       ('grape tomato','tomato, grape', 'produce',),
                       ('cherry tomato','tomato, cherry', 'produce',),
                       ('spaghetti','spaghetti', 'pastas',),
                       ('cottage cheese','cheese, cottage', 'dairy',),
                       ('white onion','onion, white', 'produce',),
                       ('baking soda','baking soda', 'baking',),
                       ('garam masala','garam masala', 'spices',),
                       ('yogurt','yogurt', 'dairy',),
                       ('monkfish','monkfish', 'seafood',),
                       ('croutons','croutons', 'bread',),
                       ('ground coriander','coriander, ground', 'spices',),
                       ('chili powder','chili powder', 'spices',),
                       ('curly lettuce leaf','lettuce, curly leaf', 'produce',),
                       ('dark sugar brown','sugar, dark brown', 'baking',),
                       ('rice vinegar','vinegar, rice', 'international',),
                       ('pasta','pasta', 'pastas',),
                       ('sesame oil','oil, sesame', 'wines&oils',),
                       ('water','water', ''),
                       ('sour cream','sour cream', 'dairy',),
                       ('orange juice','orange juice', 'produce',),
                       ('spinach','spinach', 'produce',),
                       ('stick cinnamon','cinnamon, stick', 'spices',),
                       ('shrimp paste','shrimp paste', 'international',),
                       ('ground cinnamon','cinnamon, ground', 'spices',),
                       ('salad greens','salad greens', 'produce',),
                       ('garlic','garlic', 'produce',),
                       ('vegetable oil','oil, vegetable', 'wines&oils',),
                       ('peanut butter','peanut butter', 'bread',),
                       ('seeds ajowan','ajowan, seeds', 'spices',),
                       ('apple','apple', 'produce',),
                       ('cayenne','cayenne', 'spices',),
                       ('arugula','arugula', 'produce',),
                       ('linguine pasta','pasta, linguine', 'pastas',),
                       ('scallion','scallion', 'produce',),
                       ('egg','egg', 'dairy',),
                       ('lime','lime', 'produce',),
                       ('olives','olives', 'produce',),
                       ('basil, thai fresh','basil, fresh, thai', 'produce',),
                       ('bean sprouts','bean sprouts', 'produce',),
                       ('ricotta cheese','cheese, ricotta', 'dairy',),
                       ('parsley','parsley', 'produce',),
                       ('acorn squash','squash, acorn', 'produce',),
                       ('yellow onion','onion, yellow', 'produce',),
                       ('chiles, dried red','chiles, red, dried', 'produce',),
                       ('portobello mushroom','mushroom, portobello', 'produce',),
                       ('nappa cabbage','cabbage, nappa', 'produce',),
                       ('lime leaves','lime leaves', 'produce',),
                       ('butter','butter', 'dairy',),
                       ('bell red pepper','bell pepper, red', 'produce',),
                       ('mushroom','mushroom', 'produce',),
                       ('shallot','shallot', 'produce',),
                       ('cheddar cheese','cheese, cheddar', 'dairy',),
                       ('mozzarella cheese','cheese, mozzarella', 'dairy',),
                       ('squash','squash', 'produce',),
                       ('fish sauce','fish sauce', 'international',),
                       ('green curry paste','green curry paste', 'international',),
                       ('curly endive','endive, curly', 'produce',),
                       ('white sugar','sugar, white', 'baking',),
                       ('fresh cheese white goat','cheese, fresh white goat', 'dairy',),
                       ('cilantro stems','cilantro stems', 'produce',),
                       ('yellow cornmeal','cornmeal, yellow', 'baking',),
                       ('paprika','paprika', 'spices',),
                       ('chocolate chips','chocolate chips', 'baking',),
                       ('star anise','star anise', 'spices',),
                       ('brown sugar','sugar, brown', 'baking',),
                       ('roasted peanuts','peanuts, roasted', 'produce',),
                       ('fresh cilantro','cilantro, fresh', 'produce',),
                       ('honey','honey', 'baking',),
                       ('russet potato','potato, russet', 'produce',),
                       ('lemon juice','lemon juice', 'produce',),
                       ('carrot','carrot', 'produce',),
                       ('penne pasta','pasta, penne', 'pastas',),
                       ('red onion','onion, red', 'produce',),
                       ('shredded coconut','coconut, shredded', 'baking',),
                       ('peppered linguini','linguini, peppered', 'pastas',),
                       ('milk','milk', 'dairy',),
                       ('tahitian squash','squash, tahitian', 'produce',),
                       ('baking powder','baking powder', 'baking',),
                       ('tomato sauce','tomato sauce', 'soups&sauces',),
                       ('seeds mustard','mustard, seeds', 'spices',),
                       ('flat rice flour noodles','flat rice flour noodles', 'international',),
                       ('parmesan cheese','cheese, parmesan', 'pastas',),
                       ('mayonnaise','mayonnaise', 'bread',),
                       ('leek','leek', 'produce',),
                       ('zucchini','zucchini', 'produce',),
                       ('smoked cheese Gouda','cheese, smoked Gouda', 'dairy',),
                       ('lime juice','lime juice', 'produce',),
                       ('coconut milk','coconut milk', 'international',),
                       ('eggs','egg', 'dairy',),
                       ('salmon','salmon', 'seafood',),
                       ('lasagna pasta noodles','pasta, lasagna noodles', 'pastas',),
                       ('all flour purpose','flour, all purpose', 'baking',),
                       ('ground cumin','cumin, ground', 'spices',),
                       ('cucumber','cucumber', 'produce',),
                       ('salsa','salsa', 'international',),
                       ('broccoli','broccoli', 'produce',),
                       ('rolled oats','rolled oats', 'pastas',),
                       ('tomato','tomato', 'produce',),
                       ('potato','potato', 'produce',),
                       ('white wine','wine, white', 'wines&oils',),
                       ('black ground pepper','black pepper, ground', 'spices',),
                       ('seeds cumin','cumin, seeds', 'spices',),
                       ('soy sauce','soy sauce', 'international',),
                       ('sesame seeds','sesame seeds', 'international',),
                       ('radicchio','radicchio', 'produce',),
                       ('salt','salt', 'baking',),
                       ('fresh ginger','ginger, fresh', 'produce',),
                       ('turmeric','turmeric', 'spices',),
                       ('chicken breast' ,'chicken, breast' , 'meats',),
                       ('whole chicken' ,'chicken, whole' , 'meats',),
                       ('chicken leg' ,'chicken, leg' , 'meats',),
                       ('beef' ,'beef' , 'meats',),
                       ('ground beef' ,'beef, ground' , 'meats',),
                       ('pork' ,'pork' , 'meats',),
                       ('turkey' ,'turkey' , 'meats',),
                       ]

    CONVERTER_TABLE = {
        ("c", "Tbs."):16,
        ("lb", "oz."):16,
        ("Tbs", "tsp."):3,
        ("pt", "c."):2,
        ("qt", "c."):4,
        ("gallon", "qt."):4,
        #("l", "qt."):1.057,
        ('qt.','l'):0.946,
        ('Japanese cup','ml'):200,
        ('metric cup','ml'):250,
        ('imperial cup','ml'):284.130625,
        ('Imperial pint','oz'):20,
        ("l", "ml"):1000,
        ("l", "cl"):100,
        ("l", "dl"):10,
        ("oz", "g"):28.35,
        ("kg", "g"):1000,
        ("g", "mg"):1000,
        ("tsp", "drop"):76,
        ("oz", "dram"):16,
        ("dram", "grains"):27.34375,
        ("peck", "gallon"):2,
        ("bucket", "peck"):2,
        ("bushel", "bucket"):2,
        ("lb", "grains"):7000}

    DENSITY_TABLE={
        "water":1,
        "juice, grape":1.03,
        "vegetable broth":1,
        "broth, vegetable":1,
        "broth, chicken":1,
        "milk":1.029,
        "milk, whole":1.029,
        "milk, skim":1.033,
        "milk, 2%":1.031,
        "milk, 1%":1.03,
        "coconut milk":0.875,
        "buttermilk":1.03,
        "heavy cream":0.994,
        "light cream":1.012,
        "half and half":1.025,
        "honey":1.420,
        "sugar, white":1.550,
        "salt":2.165,
        "butter":0.911,
        "oil, vegetable":0.88,
        "oil, olive":0.88,
        "oil, corn":0.88,
        "oil, sesame":0.88,
        "flour, all purpose": 0.6,
        "flour, whole wheat": 0.6,
        "corn starch": 0.6,
        "sugar, powdered": 0.6,
        "sugar, confectioners": 0.6
                }

    UNITS = [("",       ["each",   "eaches",  "ea",   "ea."]),
             ("bucket", ["bucket", "buckets", "bckt", "bckt."]),
             ("peck",   ["peck",   "pecks"]),
             ("bushel", ["bushel", "bushels", "bshl", "bshl.", "bsh", "bsh.", "bu", "bu."]),
             ("grains", ["grain",  "grains"]),
             ("dram",   ["dram",   "drams"]),
             ("drop",   ["drop",   "drops"]),
             ("fl oz",  ["fl oz",      "fluid ounce","fluid ounces","fl ounces",   "fl. ounces","fl. oz",     "fl oz.",     "fl. oz."]),
             ("tsp",    ["teaspoon",   "teaspoons",  "tea_spoon",   "tea_spoons",  "Teaspoon",  "Teaspoons",  "Tea_spoon",  "Tea_spoons",  "tsps","tsps.","Tsps","Tsps.","tsp","tsp.","Tsp","Tsp.","ts","ts.","Ts","Ts.","t","t."]),
             ("Tbs",    ["tablespoon", "tablespoons","table_spoon", "table_spoons","Tablespoon","Tablespoons","Table_spoon","Table_spoons","tbsp","tbsp.","Tbsp","Tbsp.","tbs","tbs.","Tbs","Tbs.","tb","tb.","Tb","Tb.","T","T."]),
             ("lb",     ["pound",      "pounds",     "lbs",  "lbs.",  "lb",  "lb."]),
             ("oz",     ["ounce",      "ounces",     "oz",   "oz."]),
             ("c",      ["cup",        "cups",       "c."]),
             ("qt",     ["quart",      "quarts",     "qt.",  "Qt", "Qt."]),
             ("pt",     ["pint",       "pints",      "pt.",  "Pt", "Pt."]),
             ("gallon", ["gallon",     "gallons",    "gal",  "gal."]),
             ("ml",     ["mililiter",  "mililiters", "ml",   "ml."]),
             ("cl",     ["centiliter", "centiliters","cl",   "cl."]),
             ("dl",     ["deciliter",  "deciliters", "dl",   "dl."]),
             ("l",      ["liter",      "liters",     "lit.", "l", "l."]),
             ("g",      ["grams",    "gram",      "g.", "g", "gr", "gr."]),
             ("mg",     ["miligram", "miligrams", "mg", "mg."]),
             ("kg",     ["kilogram", "kilograms", "kg", "kg."]),
             # These names aren"t really convertible, but we want them to
             # be recognized as units.
             ("small",  ["small",  "Small",    "sm",  "sm."]),
             ("medium", ["medium", "Medium",   "med", "med.", "Med", "Med."]),
             ("large",  ["large",  "Large",    "lg",  "lg.",  "Lg",  "Lg."]),
             ("box",    ["box",    "Box",      "bx"]),
             ("whole",  ["whole",  "whl",      "wh."]),
             ("clove",  ["clove",  "cloves",   "clv",    "clv."]),
             ("can",    ["can",    "Can",      "cn",      "cn."]),
             ("head",   ["head",   "heads",    "Head",    "Heads",    "hd",       "hd."]),
             ("package",["pkg.",   "package",  "Package", "packages", "Packages", "pkg", "Pkg.", "pack"]),
             ("slice",  ["slice",  "slices"]),
             ("bunch",  ["bunch",  "bunches"]),
             ]

    METRIC_RANGE = (1,999)

    UNIT_GROUPS = {
        'metric mass':[('mg',METRIC_RANGE),
                       ('g',METRIC_RANGE),
                       ('kg',(1,None))],
        'metric volume':[('ml',METRIC_RANGE),
                         ('cl',(1,99)),
                         ('dl',(1,9)),
                         ('l',(1,None)),],
        'imperial weight':[('grain',(0,27)),
                           ('dram',(0.5,15)),
                           ('oz',(0.25,15)),
                           ('lb',(0.25,None)),
                           ],
        'imperial volume':[('drop',(0,10)),
                           ('tsp',(0.125,5.9)),
                           ('Tbs',(1,4)),
                           ('c',(0.25,4)),
                           ('pt',(1,1)),
                           ('qt',(1,3)),
                           ('gallon',(1,None)),
                           ('peck',(1,2)),
                           ('bucket',(1,2)),
                           ('bushel',(1,None))]
        }


    CROSS_UNIT_TABLE = {
        ## This if for units that require an additional
        ## bit of information -- i.e. to convert between
        ## volume and mass you need the density of an
        ## item.  In these cases, the additional factor
        ## will be provided as an 'item' that is then looked
        ## up in the dictionary referenced here (i.e. the density_table)
        ## currently, 'density' is the only keyword used
        ("pt", "lb") :  ('density',1),
        ("Tbs", "oz"):  ('density',0.5),
        ("c", "oz")  :  ('density',8),
        ("pt", "oz") :  ('density',16),
        ("ml", "g")  :  ('density',1),
        }

    VOL_TO_MASS_TABLE = {
        ("pt.", "lb") : 1,
        ("Tbs.", "oz") : 0.5,
        ("c", "oz") : 8,
        ("pt", "oz") : 16,
        ("ml", "g") : 1,
        ("ml", "mg") : 1000,
        ("ml", "kg"): 0.001,
        ("cl", "kg"): 0.01,
        ("cl", "g") : 10,
        ("dl", "kg") : 0.1,
        ("dl", "g") : 100,
        ("l", "kg") : 1}

    irregular_plurals={
        "geese":"goose",
        }
    import re
    two_digit_plural_matcher = re.compile('[szxo]es$')
    one_digit_plural_matcher = re.compile("[^s]s$")
    v_plural_matcher = re.compile('ves')

    @staticmethod
    def guess_singulars (s):
        if len(s)<3: return []
        rets = []
        if s in Language.irregular_plurals:
            rets.append(Language.irregular_plurals[s])
        if Language.two_digit_plural_matcher.search(s):
            wrd=s[0:-2]
            if wrd not in rets: rets.append(wrd)
        if Language.v_plural_matcher.search(s):
            rets.append(s[0:-3]+'f')
        if Language.one_digit_plural_matcher.search(s): rets.append(s[0:-1])
        return rets

    @staticmethod
    def guess_plurals (s):
        if not s: return []
        ret = [s+'s',s+'es']
        if s[-1]=='f': ret.append(s[0:-1]+'ves')
        return ret

    IGNORE = ["and","with","of","for","cold","warm","finely","thinly","roughly","coarsely"]

    NUMBERS = {
        (1.0/8):['eighth','an eigth'],
        (1.0/4):['quarter','a quarter'],
        (3.0/4):['three quarters'],
        (2.0/3):['two thirds'],
        (1.0/3):['third','a third'],
        (1.0/2):['half','a half','one half'],
        1:['an','a','one'],
        2:['two','a couple','a couple of','a pair of'],
        3:['three'],
        4:['four'],
        5:['five'],
        6:['six'],
        7:['seven'],
        8:['eight'],
        9:['nine'],
        10:['ten'],
        11:['eleven'],
        12:['twelve','a dozen'],
        20:['twenty'],
        30:['thirty'],
        40:['forty'],
        50:['fifty'],
        60:['sixty'],
        }
