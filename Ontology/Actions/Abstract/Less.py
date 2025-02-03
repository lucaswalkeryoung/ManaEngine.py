# --------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Actions :: Abstract :: Less -----------------------------
# --------------------------------------------------------------------------------------------------
from . Abstract import Abstract

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Abstract :: Less ----------------------------------------
# --------------------------------------------------------------------------------------------------
class Less(Abstract):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'less': True, **axes})