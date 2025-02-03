# --------------------------------------------------------------------------------------------------
# ---------------------------------- Ontology :: Zones :: Library ----------------------------------
# --------------------------------------------------------------------------------------------------
from .. Objects.Card import Card
from .. Bases.Meta import Meta
from .. Bases.Axes import Axes
from .. Bases.Node import Node

from . Zone import Zone

from typing import Optional


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Zone :: Library -----------------------------------------
# --------------------------------------------------------------------------------------------------
class Library(Zone):

    def __init__(self, meta: Optional[Meta] = None, axes: Optional[Axes] = None) -> None:
        super().__init__((meta or {}), (axes or {}) | {'library': True})

        self.cards = []

    def insert(self, card: Card) -> None:

        self.connect(card, {'container': True})
        card.connect(self, {'contained': True})

        self.cards.append(card)

    def pop(self) -> None:

        card = self.cards.pop()

        self.disconnect(card)
        card.disconnect(self)

        return card


    def compile(self, parent: Node) -> Node:

        super().compile(parent)

        for name, card in self.meta.items():
            card.compile(self)