# --------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Actions :: Concrete :: Reveal ----------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Concrete :: Reveal ---------------------------------------
# --------------------------------------------------------------------------------------------------
class Reveal(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'reveal': True, **axes})