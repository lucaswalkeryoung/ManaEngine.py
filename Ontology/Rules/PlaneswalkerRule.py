# --------------------------------------------------------------------------------------------------
# ----------------------------- Ontology :: Rules :: PlaneswalkerRule ------------------------------
# --------------------------------------------------------------------------------------------------
from . Rule import Rule

from ... Bases.Node.Meta import Meta
from ... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------ Rule :: PlaneswalkerRule ------------------------------------
# --------------------------------------------------------------------------------------------------
class PlaneswalkerRule(Rule):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'planeswalker-rule': True, **axes})