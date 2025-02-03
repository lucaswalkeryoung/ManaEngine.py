# --------------------------------------------------------------------------------------------------
# -------------------------- Ontology :: Actions :: Activated :: Receive ---------------------------
# --------------------------------------------------------------------------------------------------
from . Activated import Activated

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# -------------------------------------- Activated :: Receive --------------------------------------
# --------------------------------------------------------------------------------------------------
class Receive(Activated):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'receive': True, **axes})