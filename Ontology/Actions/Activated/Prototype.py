# --------------------------------------------------------------------------------------------------
# ------------------------- Ontology :: Actions :: Activated :: Prototype --------------------------
# --------------------------------------------------------------------------------------------------
from . Activated import Activated

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------- Activated :: Prototype -------------------------------------
# --------------------------------------------------------------------------------------------------
class Prototype(Activated):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'prototype': True, **axes})