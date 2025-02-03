# --------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Components :: Cost ---------------------------------
# --------------------------------------------------------------------------------------------------
from . Component import Component

from ... Bases.Node.Meta import Meta
from ... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Component :: Cost ----------------------------------------
# --------------------------------------------------------------------------------------------------
class Cost(Component):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'cost': True, **axes})