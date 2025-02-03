# --------------------------------------------------------------------------------------------------
# -------------------------------- Ontology :: Pools :: EmblemPool ---------------------------------
# --------------------------------------------------------------------------------------------------
from .. Bases.Meta import Meta
from .. Bases.Axes import Axes

from . Pool import Pool


# --------------------------------------------------------------------------------------------------
# --------------------------------------- Pool :: EmblemPool ---------------------------------------
# --------------------------------------------------------------------------------------------------
class EmblemPool(Pool):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'emblem-pool': True, **axes})