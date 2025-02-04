# --------------------------------------------------------------------------------------------------
# ------------------------- Ontology :: Actions :: Concrete :: Proliferate -------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------ Concrete :: Proliferate -------------------------------------
# --------------------------------------------------------------------------------------------------
class Proliferate(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'proliferate': True, **axes})