def file_to_binary(file_path):
    """
    Читает файл и возвращает его содержимое в виде бинарных данных (bytes).

    :param file_path: Путь к файлу.
    :return: Объект типа bytes, содержащий бинарные данные.
    """
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
            return binary_data
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {file_path}")
        return None

jpeg_file_path = '/Users/macuser/Downloads/CatPhoto.jpeg'
binary_content = file_to_binary(jpeg_file_path)

if binary_content:
    print(f"Файл '{jpeg_file_path}' успешно преобразован в бинарные данные.")
    print(f"Тип данных: {type(binary_content)}")
    print(f"Первые 20 байт: {binary_content[:20]}")
    print(binary_content)
