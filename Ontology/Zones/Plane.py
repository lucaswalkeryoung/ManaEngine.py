# --------------------------------------------------------------------------------------------------
# ----------------------------------- Ontology :: Zones :: Plane -----------------------------------
# --------------------------------------------------------------------------------------------------
from . Battlefield import Battlefield
from . Stack import Stack
from . Exile import Exile
from . Zone  import Zone

from .. Bases.Meta import Meta
from .. Bases.Axes import Axes
from .. Bases.Edge import Edge
from .. Bases.Node import Node

from .. Objects.Player import Player
from .. Objects.Card import Card

from typing import Optional


# --------------------------------------------------------------------------------------------------
# ----------------------------------------- Zone :: Plane ------------------------------------------
# --------------------------------------------------------------------------------------------------
class Plane(Zone):

    def __init__(self, meta: Optional[Meta] = None, axes: Optional[Axes] = None) -> None:
        super().__init__((meta or {}), (axes or {}) | {'player': True})

        self.meta['battlefield'] = Battlefield()
        self.meta['exile'] = Exile()
        self.meta['stack'] = Stack()

    def compile(self, parent: Optional[Node] = None) -> Node:

        for name, player in self.meta.items():
            player.compile(self)

