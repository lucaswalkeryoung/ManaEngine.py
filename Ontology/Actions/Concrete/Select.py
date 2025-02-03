# --------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Actions :: Concrete :: Select ----------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Concrete :: Select ---------------------------------------
# --------------------------------------------------------------------------------------------------
class Select(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'select': True, **axes})