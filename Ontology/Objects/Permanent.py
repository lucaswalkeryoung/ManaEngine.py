# --------------------------------------------------------------------------------------------------
# -------------------------------- Ontology :: Objects :: Permanent --------------------------------
# --------------------------------------------------------------------------------------------------
from .. Bases.Meta import Meta
from .. Bases.Axes import Axes

from . Object import Object


# --------------------------------------------------------------------------------------------------
# -------------------------------------- Object :: Permanent ---------------------------------------
# --------------------------------------------------------------------------------------------------
class Permanent(Object):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'permanent': True, **axes})