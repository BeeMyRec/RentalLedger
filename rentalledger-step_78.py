# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: RentalLedger
import os, json


def _load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def _save(path, data):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, path)


def read_properties(db_path='data/ledger.json'):
    return _load(db_path).get('properties', [])


def write_properties(properties):
    db = {'properties': properties}
    _save('data/ledger.json', db)


def read_tenants(db_path='data/ledger.json'):
    return _load(db_path).get('tenants', [])


def write_tenants(tenants):
    db = {'tenants': tenants}
    _save('data/ledger.json', db)


def read_payments(db_path='data/ledger.json'):
    return _load(db_path).get('payments', [])


def write_payments(payments):
    db = {'payments': payments}
    _save('data/ledger.json', db)


def read_maintenance(db_path='data/ledger.json'):
    return _load(db_path).get('maintenance', [])


def write_maintenance(maintenance):
    db = {'maintenance': maintenance}
    _save('data/ledger.json', db)


def read_documents(db_path='data/ledger.json'):
    return _load(db_path).get('documents', {})


def write_documents(documents):
    db = {'documents': documents}
    _save('data/ledger.json', db)
