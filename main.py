from Ontology.Zones.Battlefield import Battlefield
from Ontology.Zones.Plane import Plane
from Ontology.Zones.Stack import Stack
from Ontology.Zones.Exile import Exile

from Ontology.Objects.Player import Player

game = Plane({
    'player-1': Player({}),
    'player-2': Player({}),
}).compile()