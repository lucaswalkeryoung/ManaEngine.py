# --------------------------------------------------------------------------------------------------
# ------------------------- Ontology :: Actions :: Triggered :: Gravestorm -------------------------
# --------------------------------------------------------------------------------------------------
from . Triggered import Triggered

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------ Triggered :: Gravestorm -------------------------------------
# --------------------------------------------------------------------------------------------------
class Gravestorm(Triggered):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'gravestorm': True, **axes})