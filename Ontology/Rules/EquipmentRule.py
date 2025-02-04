# --------------------------------------------------------------------------------------------------
# ------------------------------- Ontology :: Rules :: EquipmentRule -------------------------------
# --------------------------------------------------------------------------------------------------
from . Rule import Rule

from ... Bases.Node.Meta import Meta
from ... Bases.Node.Axes import Axes


# --------------------------------------------------------------------------------------------------
# ------------------------------------- Rule :: EquipmentRule --------------------------------------
# --------------------------------------------------------------------------------------------------
class EquipmentRule(Rule):

    def __init__(self, meta: Meta, axes: Axes) -> None:
        super().__init__(meta, {'equipment-rule': True, **axes})