# --------------------------------------------------------------------------------------------------
# -------------------------- Ontology :: Actions :: Concrete :: Sacrifice --------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------- Concrete :: Sacrifice --------------------------------------
# --------------------------------------------------------------------------------------------------
class Sacrifice(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'sacrifice': True, **axes})