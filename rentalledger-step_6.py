# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: RentalLedger
def delete_item(item_id, item_type, confirm=False):
    if not confirm:
        print(f"Удаление {item_type} с id={item_id} отменено (требуется флаг --confirm).")
        return False
    
    try:
        # Имитация удаления из базы данных или словаря
        del_db = getattr(db, item_type)  # db.properties, db.tenants и т.д.
        if item_id in del_db:
            del del_db[item_id]
            print(f"{item_type} с id={item_id} успешно удален.")
            return True
        else:
            print(f"Не найден {item_type} с id={item_id}.")
            return False
    except KeyError as e:
        print(f"Ошибка доступа к коллекции {e}: коллекция не найдена или пустая.")
        return False
