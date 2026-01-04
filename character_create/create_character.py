def create_character(name: str, strength: int, intelligence: int, charisma: int) -> str:
    # Validate name input
    if not isinstance(name, str):
        return 'The character name should be a string'
    elif name == '':
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif ' ' in name:
        return 'The character name should not contain spaces'

    # Validate stats input (must be integers)
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return 'All stats should be integers'

    # Validate that each stat is between 1 and 4
    if not (1 <= strength <= 4) or not (1 <= intelligence <= 4) or not (1 <= charisma <= 4):
        return 'All stats should be no less than 1 and no more than 4'

    # Validate that the sum of all stats is 7
    if (strength + intelligence + charisma) != 7:
        return 'The character should start with 7 points'

    # Format the result output for each stat (STR, INT, CHA)
    full_dot = '●'
    empty_dot = '○'

    # Build the formatted stat lines
    stats = [
        f'STR {full_dot * strength}{empty_dot * (10 - strength)}',
        f'INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}',
        f'CHA {full_dot * charisma}{empty_dot * (10 - charisma)}'
    ]

    # Return the formatted character name and stats
    return f"{name}\n" + "\n".join(stats)

def main():
    # Example usage:
    print(create_character('Alice', 3, 2, 2))


if __name__ == "__main__":
    main()