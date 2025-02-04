# --------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Actions :: Concrete :: Flip -----------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Concrete :: Flip ----------------------------------------
# --------------------------------------------------------------------------------------------------
class Flip(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'flip': True, **axes})