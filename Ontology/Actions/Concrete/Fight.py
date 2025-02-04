# --------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Actions :: Concrete :: Fight ----------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Concrete :: Fight ----------------------------------------
# --------------------------------------------------------------------------------------------------
class Fight(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'fight': True, **axes})