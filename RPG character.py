full_dot = '●'
empty_dot = '○'


def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return "The character name should be a string"
    elif not character_name:
        return "The character should have a name"
    elif len(character_name) > 10:
        return "The character name is too long"
    elif " " in character_name:
        return "The character name should not contain spaces"
    # using all() can take one one arguments and checks all are int
    if not all(isinstance(_, int) for _ in (strength, intelligence, charisma)):
        return "All stats should be integers"
    else:
        # use "or" not "and" because it checks even one is wrong it returns and checks everything should be wrong then only executes
        if strength < 1 or intelligence < 1 or charisma < 1:
            return "All stats should be no less than 1"
        elif strength > 4 or intelligence > 4 or charisma > 4:
            return "All stats should be no more than 4"
        elif (strength + intelligence + charisma) != 7:
            return "The character should start with 7 points"

    return  (
        f"{character_name}\n"
        f"STR {stat(strength)}\n" # I can use multiply like "(strength * full_dot + (10-strength)*empty_dot)"
        f"INT {stat(intelligence)}\n"
        f"CHA {stat(charisma)}"
    )


def stat(values):
    dots = ""
    for _ in range(10):
        if _ < values:
            dots += full_dot
        else:
            dots += empty_dot
    return dots


a = create_character("ren", 4, 2, 1)
print(a)