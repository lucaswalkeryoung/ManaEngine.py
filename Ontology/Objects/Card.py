# --------------------------------------------------------------------------------------------------
# ---------------------------------- Ontology :: Objects :: Card -----------------------------------
# --------------------------------------------------------------------------------------------------
from .. Bases.Meta import Meta
from .. Bases.Axes import Axes
from .. Bases.Node import Node
from .. Bases.Edge import Edge
from .. Zones.Zone import Zone

from . Object import Object

from typing import TYPE_CHECKING
from typing import Optional


# --------------------------------------------------------------------------------------------------
# ----------------------------------------- Object :: Card -----------------------------------------
# --------------------------------------------------------------------------------------------------
class Card(Object):

    def __init__(self, meta: Optional[Meta] = None, axes: Optional[Axes] = None) -> None:
        super().__init__((meta or {}), (axes or {}) | {'card': True})

    def compile(self, source: Node) -> Node:

        if isinstance(source, Zone):
            source.connect(self, {'container': True})
            self.connect(source, {'contained': True})

        else:
            source.connect(self, {'owner-of': True})
            self.connect(source, {'owner-by': True})