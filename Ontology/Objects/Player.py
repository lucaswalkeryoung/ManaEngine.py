# --------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Objects :: Player ----------------------------------
# --------------------------------------------------------------------------------------------------
from .. Zones.CommandZone import CommandZone
from .. Zones.Library import Library
from .. Zones.Hand import Hand
from .. Zones.Graveyard import Graveyard

from .. Pools.DamagePool import DamagePool
from .. Pools.EmblemPool import EmblemPool
from .. Pools.ManaPool import ManaPool

from .. Bases.Meta import Meta
from .. Bases.Axes import Axes
from .. Bases.Node import Node
from .. Bases.Edge import Edge

from . Object import Object
from . Card   import Card

from typing import Optional


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Object :: Player ----------------------------------------
# --------------------------------------------------------------------------------------------------
class Player(Object):

    def __init__(self, meta: Optional[Meta] = None, axes: Optional[Axes] = None) -> None:
        super().__init__((meta or {}), (axes or {}) | {'player': True})

        self.meta['command-zone'] = CommandZone()
        self.meta['library'] = Library()
        self.meta['hand'] = Hand()
        self.meta['graveyard'] = Graveyard()

        for i in range(100):

            card = Card()

            card.connect(self, {'owned-by'})
            self.connect(card, {'owner-of'})

            self.meta['library'].insert(card)

        for i in range(7):

            card = self.meta['library'].pop()
            self.meta['hand'].insert(card)

        self.axes['life']  = 40

    def compile(self, plane: Node) -> Node:

        plane.connect(self, {'occupied': True})
        self.connect(plane, {'occupier': True})

        for name, node in self.meta.items():
            node.compile(self)