# --------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Actions :: Activated :: Bestow ---------------------------
# --------------------------------------------------------------------------------------------------
from . Activated import Activated

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# -------------------------------------- Activated :: Bestow ---------------------------------------
# --------------------------------------------------------------------------------------------------
class Bestow(Activated):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'bestow': True, **axes})