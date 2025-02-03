# --------------------------------------------------------------------------------------------------
# ----------------------------------- Ontology :: Zones :: Hand ------------------------------------
# --------------------------------------------------------------------------------------------------
from .. Objects.Card import Card
from .. Bases.Meta import Meta
from .. Bases.Axes import Axes
from .. Bases.Node import Node

from . Zone import Zone

from typing import Optional


# --------------------------------------------------------------------------------------------------
# ------------------------------------------ Zone :: Hand ------------------------------------------
# --------------------------------------------------------------------------------------------------
class Hand(Zone):

    def __init__(self, meta: Optional[Meta] = None, axes: Optional[Axes] = None) -> None:
        super().__init__((meta or {}), (axes or {}) | {'hand': True})

        self.cards = []

    def insert(self, card: Card) -> None:

        self.connect(card, {'container': True})
        card.connect(self, {'contained': True})

        self.cards.append(card)

# black market
# headless rider
#