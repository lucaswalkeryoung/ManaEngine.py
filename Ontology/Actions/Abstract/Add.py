# --------------------------------------------------------------------------------------------------
# ----------------------------- Ontology :: Actions :: Abstract :: Add -----------------------------
# --------------------------------------------------------------------------------------------------
from . Abstract import Abstract

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ---------------------------------------- Abstract :: Add -----------------------------------------
# --------------------------------------------------------------------------------------------------
class Add(Abstract):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'add': True, **axes})