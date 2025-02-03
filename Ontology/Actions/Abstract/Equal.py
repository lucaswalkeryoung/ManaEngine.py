# --------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Actions :: Abstract :: Equal ----------------------------
# --------------------------------------------------------------------------------------------------
from . Abstract import Abstract

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Abstract :: Equal ----------------------------------------
# --------------------------------------------------------------------------------------------------
class Equal(Abstract):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'equal': True, **axes})