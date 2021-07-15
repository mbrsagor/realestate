from enum import IntEnum


# Type of inventory
class InventoryTypes(IntEnum):
    KG = 0
    PCS = 1
    BOX = 2

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]
