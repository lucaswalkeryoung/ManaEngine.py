# --------------------------------------------------------------------------------------------------
# ----------------------------- Ontology :: Actions :: Concrete :: Die -----------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Concrete :: Die -----------------------------------------
# --------------------------------------------------------------------------------------------------
class Die(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'die': True, **axes})