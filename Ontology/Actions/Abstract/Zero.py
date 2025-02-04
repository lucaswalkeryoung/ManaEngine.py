# --------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Actions :: Abstract :: Zero -----------------------------
# --------------------------------------------------------------------------------------------------
from . Abstract import Abstract

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Abstract :: Zero ----------------------------------------
# --------------------------------------------------------------------------------------------------
class Zero(Abstract):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'zero': True, **axes})