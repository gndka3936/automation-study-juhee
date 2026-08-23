def names(text):
    cleaned_names = []

    for name in text:
        name = name.strip()
        name = name.lower()
        cleaned_names.append(name)

    cleaned_names.sort()

    return cleaned_names