# --------------------------------------------------------------------------------------------------
# -------------------------- Ontology :: Actions :: Concrete :: Doubletap --------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------- Concrete :: Doubletap --------------------------------------
# --------------------------------------------------------------------------------------------------
class Doubletap(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'doubletap': True, **axes})