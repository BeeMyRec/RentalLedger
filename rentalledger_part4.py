# === Stage 4: Implement create operations for the primary records ===
# Project: RentalLedger
from typing import Optional, List
import uuid

class Property:
    def __init__(self, address: str, num_units: int):
        self.id = str(uuid.uuid4())[:8]
        self.address = address
        self.num_units = num_units
        self.units: dict[str, 'Unit'] = {}

    def add_unit(self, unit_num: int) -> Unit:
        if unit_num in self.units:
            return self.units[unit_num]
        unit = Unit(unit_num, self.id)
        self.units[unit_num] = unit
        return unit

class Tenant:
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.email = email

class Unit:
    def __init__(self, number: int, property_id: str):
        self.number = number
        self.property_id = property_id
        self.occupant: Optional[Tenant] = None
        self.rent_amount: float = 0.0
        self.is_occupied = False

    def assign_tenant(self, tenant: Tenant) -> bool:
        if self.occupant is not None:
            return False
        self.occupant = tenant
        self.is_occupied = True
        return True

class Payment:
    def __init__(self, amount: float, date_str: str):
        self.id = str(uuid.uuid4())[:8]
        self.amount = amount
        self.date = date_str
        self.status = 'pending'

    def confirm(self) -> None:
        if self.status == 'paid':
            return
        self.status = 'paid'

class MaintenanceRequest:
    def __init__(self, description: str, priority: int):
        self.id = str(uuid.uuid4())[:8]
        self.description = description
        self.priority = priority
        self.created_at = date.today().isoformat()
        self.status = 'open'

class Document:
    def __init__(self, name: str, file_path: str):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.file_path = file_path
