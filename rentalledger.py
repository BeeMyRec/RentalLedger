# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: RentalLedger
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional
import uuid

@dataclass
class Property:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    address: str = ""
    rent_amount: float = 0.0
    
@dataclass 
class Tenant:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    property_id: Optional[str] = None
    
@dataclass
class Payment:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    tenant_id: str = ""
    amount: float = 0.0
    due_date: date = date.today()
    
@property
def get_all_properties(self) -> List[Property]: return self._properties

@property 
def get_all_tenants(self) -> List[Tenant]: return self._tenants

class RentalLedger:
    def __init__(self):
        self._properties: dict[str, Property] = {}
        self._tenants: dict[str, Tenant] = {}
        
    def add_property(self, address: str, rent_amount: float) -> Property:
        prop = Property(address=address, rent_amount=rent_amount)
        self._properties[prop.id] = prop
        return prop
        
    def register_tenant(self, name: str, property_id: Optional[str] = None) -> Tenant:
        tenant = Tenant(name=name)
        if property_id:
            tenant.property_id = property_id
        self._tenants[tenant.id] = tenant
        return tenant
        
    def record_payment(self, tenant_id: str, amount: float, due_date: Optional[date] = None) -> Payment:
        payment = Payment(tenant_id=tenant_id, amount=amount, due_date=due_date or date.today())
        self._payments[payment.id] = payment
        return payment
        
    @property 
    def get_all_payments(self) -> List[Payment]: return list(self._payments.values())
