# --------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Actions :: Abstract :: Action ----------------------------
# --------------------------------------------------------------------------------------------------
from .... Bases.Node.Node import Node
from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes
from . Node import Node

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ----------------------------------------- Node :: Action -----------------------------------------
# --------------------------------------------------------------------------------------------------
class Action(Node):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'action': True, **axes})