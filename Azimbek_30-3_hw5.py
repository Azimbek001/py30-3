def get_born_year(name: str = None , age :int = None) -> str:
    current_year = 2023
    born_year = current_year - age
    return f'Name {name} Born : {born_year}'
get_born_year()
