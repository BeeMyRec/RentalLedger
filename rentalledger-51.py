# === Stage 51: Add unit tests for search and filter behavior ===
# Project: RentalLedger
from rental_ledger.models.property import Property
from rental_ledger.search import search_properties, filter_properties


def test_search_by_city():
    props = [
        Property(id="p1", name="Apartment A", city="Berlin"),
        Property(id="p2", name="House B", city="Munich"),
        Property(id="p3", name="Flat C", city="Berlin"),
    ]
    results = search_properties(props, "city=Berlin")
    assert len(results) == 2


def test_filter_by_status():
    props = [
        Property(id="p1", name="A", status=Property.Status.ACTIVE),
        Property(id="p2", name="B", status=Property.Status.INACTIVE),
        Property(id="p3", name="C", status=Property.Status.ACTIVE),
    ]
    results = filter_properties(props, status_filter={"status": Property.Status.ACTIVE})
    assert len(results) == 2


def test_search_with_multiple_criteria():
    props = [
        Property(id="p1", name="A", city="Berlin", status=Property.Status.ACTIVE),
        Property(id="p2", name="B", city="Munich", status=Property.Status.INACTIVE),
    ]
    results = search_properties(
        props, "city=Berlin,status=ACTIVE"
    )
    assert len(results) == 1


def test_filter_empty_result():
    props = [
        Property(id="p1", name="A", city="Berlin"),
    ]
    results = filter_properties(props, status_filter={"status": Property.Status.INACTIVE})
    assert len(results) == 0
