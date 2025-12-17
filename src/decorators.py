from functools import wraps


def log(filename="mylog.txt"):
    """ Декоратор log автоматически фиксирует:
    - Имя функции и результат выполнения функции при успешной операции.
    - Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
    Принимает необязательный аргумент filename, который определяет, куда будут записываться логи -
    в файл или в консоль."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def write_log(message):
                if filename:
                    with open(filename, 'a', encoding='utf-8') as log_file:
                        log_file.write(message + '\n')
                else:
                    print(message)

            try:
                result = func(*args, **kwargs)
                write_log(f"{func.__name__} ok")
                return result
            except Exception as e:
                write_log(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator
