# --------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Rules :: LifeRule ----------------------------------
# --------------------------------------------------------------------------------------------------
from . Rule import Rule

from ... Bases.Node.Meta import Meta
from ... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Rule :: LifeRule ----------------------------------------
# --------------------------------------------------------------------------------------------------
class LifeRule(Rule):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'life-rule': True, **axes})