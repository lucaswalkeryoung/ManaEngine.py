# --------------------------------------------------------------------------------------------------
# ----------------------------------- Ontology :: Rules :: Rule ------------------------------------
# --------------------------------------------------------------------------------------------------
from ... Bases.Node.Node import Node
from ... Bases.Node.Meta import Meta
from ... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------------ Rule :: Rule ------------------------------------------
# --------------------------------------------------------------------------------------------------
class Rule(Rule):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'rule': True, **axes})