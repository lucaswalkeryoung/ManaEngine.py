# --------------------------------------------------------------------------------------------------
# ------------------------------ Ontology :: Objects :: Effect Object ------------------------------
# --------------------------------------------------------------------------------------------------
from Ontology.Bases.Meta import Meta
from Ontology.Bases.Axes import Axes

from .  Object import Object


# --------------------------------------------------------------------------------------------------
# ------------------------------------- Class :: Effect Object -------------------------------------
# --------------------------------------------------------------------------------------------------
class Effect(Object):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, meta, axes | {'effect': True})