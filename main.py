import json

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def display_all_records(data):
    for fish in data:
        print(f"""
Номер записи: {fish['id']}, 
Общее название: {fish['name']},                       
Латинское название: {fish['latin_name']}, 
Пресноводная: {fish['is_salt_water_fish']},    
Кол-во подвидов: {fish['sub_type_count']} """)

def display_record_by_id(data, id):
    find = False
    for fish in data:
        if id == fish['id']:
            print(f"""
Номер записи: {fish['id']}, 
Общее название: {fish['name']},                       
Латинское название: {fish['latin_name']}, 
Пресноводная: {fish['is_salt_water_fish']},    
Количество подвидов: {fish['sub_type_count']} 
                """)
            find = True
            break
    if not find:
        print("Запись не найдена")

def add_record(data, new_fish):
    for fish in data:
        if fish['id'] == new_fish['id']:
            print("Такой номер уже существует")
            return False
    data.append(new_fish)
    return True

def delete_record(data, id):
    find = False
    for fish in data:
        if id == fish['id']:
            data.remove(fish)
            find = True
            break
    if find:
        print("Запись удалена")
        return True
    else:
        print("Запись не найдена")
        return False

def main():
    file_path = "fishs.json"
    data = load_data(file_path)
    operations_count = 0

    while True:
        print("""
1.Вывести все записи 
2.Вывести запись по полю 
3.Добавить запись 
4.Удалить запись по полю 
5.Выйти из программы
        """)
        num = int(input("Введите номер действия: "))

        if num == 1:
            display_all_records(data)
            operations_count += 1

        elif num == 2:
            id = int(input("Введите номер рыбы: "))
            display_record_by_id(data, id)
            operations_count += 1

        elif num == 3:
            id = int(input("Введите id рыбы: "))
            name = input("Введите общее название рыбы: ")  
            latin_name = input("Введите латинское название рыбы: ")  
            is_salt_water_fish = input("Является ли рыба пресноводной? (да/нет):  ")  
            sub_type_count = float(input("Введите количество подвидов: "))  
            new_fish = {
                'id': id,
                'name': name,
                'latin_name': latin_name,
                'is_salt_water_fish': True if is_salt_water_fish.lower() == 'да' else False, 
                'sub_type_count': sub_type_count
            }
            if add_record(data, new_fish):
                save_data(file_path, data)
                print("Запись успешно добавлена")
            operations_count += 1

        elif num == 4:
            id = int(input("Введите id рыбы: "))
            if delete_record(data, id):
                save_data(file_path, data)
            operations_count += 1

        elif num == 5:
            print(f"""Программа завершена
Количество операций: {operations_count}""")
            break

        else:
            print("Этот номер отсутствует")

if __name__ == "__main__":
    main()
