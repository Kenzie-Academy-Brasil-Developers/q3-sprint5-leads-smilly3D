from functools import wraps
from flask import request

def verify_entry_key(references_keys: str):
    def test_key(func):
        @wraps(func)
        def wraped_function():
            try:
                data = request.get_json()

                keys_test = data.keys()

                for key in keys_test:
                    if key != "email":
                        raise KeyError
                
                for value in list(data.values()):
                    if type(value) != str:
                        raise TypeError
                
                return func()
            except KeyError:
                return {
                        "error": "chave(s) incorreta(s)",
                        "expected": references_keys,
                        "received": list(data.keys())
                        }, 400
            except TypeError:
                return {
                        "error": "all values must be strings "
                        }, 400

        return wraped_function
    return test_key