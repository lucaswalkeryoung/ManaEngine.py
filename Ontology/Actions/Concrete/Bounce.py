# --------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Actions :: Concrete :: Bounce ----------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Concrete :: Bounce ---------------------------------------
# --------------------------------------------------------------------------------------------------
class Bounce(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'bounce': True, **axes})