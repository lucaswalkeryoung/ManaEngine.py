# --------------------------------------------------------------------------------------------------
# ------------------------------- Ontology :: Rules :: ToughnessRule -------------------------------
# --------------------------------------------------------------------------------------------------
from . Rule import Rule

from ... Bases.Node.Meta import Meta
from ... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------- Rule :: ToughnessRule --------------------------------------
# --------------------------------------------------------------------------------------------------
class ToughnessRule(Rule):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'toughness-rule': True, **axes})