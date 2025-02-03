# --------------------------------------------------------------------------------------------------
# ---------------------------------------- The Rules Engine ----------------------------------------
# --------------------------------------------------------------------------------------------------
from Ontology.Card import Card
from Ontology.Node import Node
from Ontology.Edge import Edge

Card({
    'precondition': Condition({
        'sunpetal-grove-enters-tapped': When({
            'unless': Empty({
                '': Block({
                    'you': Connection({'from': '~', 'with': 'controls'}, {'player': True}),
                    'control': Connection({'from': 'you', 'with': 'controls'}, {'land': True}),
                    'plains': Filter({'': 'you-control'}, {'plains': True}),
                    'forest': Filter({'': 'you-control'}, {'forest': True}),
                    'either': Concat({'plains': 'plains', 'forest': 'forest'}),
                }),
            }),
            'otherwise': Tap({'': '~'})
        }),
    }),
    '{T}': Ability({
        'add': Select({
            'either': Enlist({
                '{W}': Add(axes={'white': True}),
                '{G}': Add(axes={'green': True}),
            }),
        }),
    }, {'activated': True, 'mana': True}),
}, {'name': "Sunpetal Grove", 'land': True, 'nonbasic': True})