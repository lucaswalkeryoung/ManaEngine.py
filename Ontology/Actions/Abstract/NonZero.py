# --------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Actions :: Abstract :: NonZero ---------------------------
# --------------------------------------------------------------------------------------------------
from . Abstract import Abstract

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# -------------------------------------- Abstract :: NonZero ---------------------------------------
# --------------------------------------------------------------------------------------------------
class NonZero(Abstract):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'non-zero': True, **axes})