# --------------------------------------------------------------------------------------------------
# -------------------------- Ontology :: Actions :: Triggered :: Rebound ---------------------------
# --------------------------------------------------------------------------------------------------
from . Triggered import Triggered

from .... Bases.Node.Meta import Meta
from .... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# -------------------------------------- Triggered :: Rebound --------------------------------------
# --------------------------------------------------------------------------------------------------
class Rebound(Triggered):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'rebound': True, **axes})