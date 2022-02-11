import re


def validNumber(phone_nuber):
    pattern = re.compile("^\\([\d]{2}\\)[\d]{5}-[\d]{5}$", re.IGNORECASE)
    return pattern.match(phone_nuber) is not None

