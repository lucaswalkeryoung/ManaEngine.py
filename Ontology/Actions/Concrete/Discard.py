# --------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Actions :: Concrete :: Discard ---------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# -------------------------------------- Concrete :: Discard ---------------------------------------
# --------------------------------------------------------------------------------------------------
class Discard(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'discard': True, **axes})