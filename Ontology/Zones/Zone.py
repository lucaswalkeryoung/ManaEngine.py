# --------------------------------------------------------------------------------------------------
# ----------------------------------- Ontology :: Zones :: Zone ------------------------------------
# --------------------------------------------------------------------------------------------------
from .. Bases.Node import Node
from .. Bases.Meta import Meta
from .. Bases.Axes import Axes

from typing import Optional


# --------------------------------------------------------------------------------------------------
# ------------------------------------------ Zone :: Zone ------------------------------------------
# --------------------------------------------------------------------------------------------------
class Zone(Node):

    def __init__(self, meta: Optional[Meta] = None, axes: Optional[Axes] = None) -> None:
        super().__init__((meta or {}), (axes or {}) | {'zone': True})

    def compile(self, parent: 'Node') -> 'Node':

        parent.connect(self, {'zone-of': True})
        self.connect(parent, {'zone-to': True})