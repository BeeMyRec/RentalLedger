# === Stage 64: Add validation for relationship references ===
# Project: RentalLedger
class ValidationError(Exception):
    pass


def validate_references(data, model_class):
    if 'property_id' in data and 'tenant_id' in data:
        if isinstance(model_class, type) and issubclass(model_class, ModelBase):
            for attr_name in ('property_id', 'tenant_id'):
                val = data.get(attr_name)
                if val is not None and not isinstance(val, int):
                    raise ValidationError(f"{attr_name} must be an integer or null")
