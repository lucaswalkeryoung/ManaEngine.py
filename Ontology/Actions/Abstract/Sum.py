# --------------------------------------------------------------------------------------------------
# ----------------------------- Ontology :: Actions :: Abstract :: Sum -----------------------------
# --------------------------------------------------------------------------------------------------
from . Abstract import Abstract

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Abstract :: Sum -----------------------------------------
# --------------------------------------------------------------------------------------------------
class Sum(Abstract):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'sum': True, **axes})