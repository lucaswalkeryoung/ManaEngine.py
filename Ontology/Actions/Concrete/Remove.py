# --------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Actions :: Concrete :: Remove ----------------------------
# --------------------------------------------------------------------------------------------------
from . Concrete import Concrete

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Concrete :: Remove ---------------------------------------
# --------------------------------------------------------------------------------------------------
class Remove(Concrete):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'remove': True, **axes})