# --------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Actions :: Abstract :: Filter ----------------------------
# --------------------------------------------------------------------------------------------------
from . Abstract import Abstract

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Abstract :: Filter ---------------------------------------
# --------------------------------------------------------------------------------------------------
class Filter(Abstract):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'filter': True, **axes})