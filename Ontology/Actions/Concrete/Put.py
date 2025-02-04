# --------------------------------------------------------------------------------------------------
# ----------------------------- Ontology :: Actions :: Concrete :: Put -----------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Concrete :: Put -----------------------------------------
# --------------------------------------------------------------------------------------------------
class Put(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'put': True, **axes})