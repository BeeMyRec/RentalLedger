# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: RentalLedger
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List
import uuid

@dataclass
class Property:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    address: str = ""
    rent_amount: float = 0.0
    status: str = "active"

@dataclass
class Tenant:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    email: str = ""
    phone: Optional[str] = None

@dataclass
class Payment:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    tenant_id: str = ""
    property_id: str = ""
    amount: float = 0.0
    due_date: date = field(default_factory=date)
    paid_date: Optional[date] = None

@dataclass
class MaintenanceRequest:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    property_id: str = ""
    description: str = ""
    status: str = "open"
    created_at: date = field(default_factory=date)
