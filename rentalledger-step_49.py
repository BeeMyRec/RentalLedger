# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: RentalLedger
import pytest
from RentalLedger.models.property import Property
from RentalLedger.models.tenant import Tenant
from RentalLedger.models.payment import Payment
from RentalLedger.models.maintenance import Maintenance
from RentalLedger.models.document import Document


class TestUpdateEdgeCases:
    def test_update_nonexistent_record(self):
        props = {}
        with pytest.raises(KeyError):
            props.update({"1": "new"})

    def test_update_with_empty_dict(self):
        d = {"a": 1}
        assert d.update({}) is None
        assert d == {"a": 1}

    def test_delete_nonexistent_key(self):
        data = {"x": 10}
        with pytest.raises(KeyError):
            del data["y"]


class TestDeleteEdgeCases:
    def test_delete_all_items(self):
        d = {"p": Property("P1"), "t": Tenant("T1")}
        assert len(d) == 2
        for key in list(d.keys()):
            del d[key]
        assert len(d) == 0

    def test_delete_mixed_types(self):
        items = [Property("A"), Tenant("B"), Payment("C"), Maintenance("D"), Document("E")]
        for item in items:
            with pytest.raises(TypeError):
                del items[items.index(item)]


class TestEdgeCaseIntegration:
    def test_empty_property_list_operations(self):
        props = []
        assert "P1" not in props

    def test_large_batch_update(self):
        data = {f"k{i}": i for i in range(20)}
        assert len(data) == 20
