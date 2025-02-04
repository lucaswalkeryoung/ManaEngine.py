# --------------------------------------------------------------------------------------------------
# ------------------------- Ontology :: Actions :: Activated :: Aftermath --------------------------
# --------------------------------------------------------------------------------------------------
from . Activated import Activated

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------- Activated :: Aftermath -------------------------------------
# --------------------------------------------------------------------------------------------------
class Aftermath(Activated):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'aftermath': True, **axes})