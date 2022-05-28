def type_effectiveness(atk_type, def_type1, def_type2):
    # BASE EFFECTIVNESS IS ASSUMED TO BE 1
    total_effectivness = 1

    # GET ATTACK TYPE
    atk_type = atk_type.upper()

    # GET DEFENDING TYPES
    def_type1 = def_type1.upper()
    # MAKE SURE ITS A STRING AND NOT NaN (FLOAT)
    if isinstance(def_type2, float) or def_type2 is None:
        def_type2 = ""
    else:
        def_type2 = def_type2.upper()

    # LOTS OF IF STATEMENTS FOR THE TYPE CHART
    if atk_type == "NORMAL":
        if def_type1 == "ROCK" or def_type2 == "ROCK":
            total_effectivness *= 0.5
        elif def_type1 == "GHOST" or def_type2 == "GHOST":
            total_effectivness *= 0

    if atk_type == "FIRE":
        if def_type1 == "FIRE" or def_type2 == "FIRE":
            total_effectivness *= 0.5
        if def_type1 == "WATER" or def_type2 == "WATER":
            total_effectivness *= 0.5
        if def_type1 == "GRASS" or def_type2 == "GRASS":
            total_effectivness *= 2
        if def_type1 == "ICE" or def_type2 == "ICE":
            total_effectivness *= 2
        if def_type1 == "BUG" or def_type2 == "BUG":
            total_effectivness *= 2
        if def_type1 == "ROCK" or def_type2 == "ROCK":
            total_effectivness *= 0.5
        if def_type1 == "DRAGON" or def_type2 == "DRAGON":
            total_effectivness *= 0.5

    if atk_type == "WATER":
        if def_type1 == "FIRE" or def_type2 == "FIRE":
            total_effectivness *= 2
        if def_type1 == "WATER" or def_type2 == "WATER":
            total_effectivness *= 0.5
        if def_type1 == "GRASS" or def_type2 == "GRASS":
            total_effectivness *= 0.5
        if def_type1 == "GROUND" or def_type2 == "GROUND":
            total_effectivness *= 2
        if def_type1 == "ROCK" or def_type2 == "ROCK":
            total_effectivness *= 2
        if def_type1 == "DRAGON" or def_type2 == "DRAGON":
            total_effectivness *= 0.5

    if atk_type == "ELECTRIC":
        if def_type1 == "WATER" or def_type2 == "WATER":
            total_effectivness *= 2
        if def_type1 == "ELECTRIC" or def_type2 == "ELECTRIC":
            total_effectivness *= 0.5
        if def_type1 == "GRASS" or def_type2 == "GRASS":
            total_effectivness *= 0.5
        if def_type1 == "GROUND" or def_type2 == "GROUND":
            total_effectivness *= 0
        if def_type1 == "FLYING" or def_type2 == "FLYING":
            total_effectivness *= 2
        if def_type1 == "DRAGON" or def_type2 == "DRAGON":
            total_effectivness *= 0.5

    if atk_type == "GRASS":
        if def_type1 == "FIRE" or def_type2 == "FIRE":
            total_effectivness *= 0.5
        if def_type1 == "WATER" or def_type2 == "WATER":
            total_effectivness *= 2
        if def_type1 == "GRASS" or def_type2 == "GRASS":
            total_effectivness *= 0.5
        if def_type1 == "POISON" or def_type2 == "POISON":
            total_effectivness *= 0.5
        if def_type1 == "GROUND" or def_type2 == "GROUND":
            total_effectivness *= 2
        if def_type1 == "FLYING" or def_type2 == "FLYING":
            total_effectivness *= 0.5
        if def_type1 == "BUG" or def_type2 == "BUG":
            total_effectivness *= 0.5
        if def_type1 == "ROCK" or def_type2 == "ROCK":
            total_effectivness *= 2
        if def_type1 == "DRAGON" or def_type2 == "DRAGON":
            total_effectivness *= 0.5

    if atk_type == "ICE":
        if def_type1 == "WATER" or def_type2 == "WATER":
            total_effectivness *= 0.5
        if def_type1 == "GRASS" or def_type2 == "GRASS":
            total_effectivness *= 2
        if def_type1 == "ICE" or def_type2 == "ICE":
            total_effectivness *= 0.5
        if def_type1 == "GROUND" or def_type2 == "GROUND":
            total_effectivness *= 2
        if def_type1 == "GROUND" or def_type2 == "GROUND":
            total_effectivness *= 2
        if def_type1 == "DRAGON" or def_type2 == "DRAGON":
            total_effectivness *= 2

    if atk_type == "FIGHTING":
        if def_type1 == "NORMAL" or def_type2 == "NORMAL":
            total_effectivness *= 2
        if def_type1 == "ICE" or def_type2 == "ICE":
            total_effectivness *= 2
        if def_type1 == "POISON" or def_type2 == "POISON":
            total_effectivness *= 0.5
        if def_type1 == "FLYING" or def_type2 == "FLYING":
            total_effectivness *= 0.5
        if def_type1 == "PSYCHIC" or def_type2 == "PSYCHIC":
            total_effectivness *= 0.5
        if def_type1 == "BUG" or def_type2 == "BUG":
            total_effectivness *= 0.5
        if def_type1 == "ROCK" or def_type2 == "ROCK":
            total_effectivness *= 2
        if def_type1 == "GHOST" or def_type2 == "GHOST":
            total_effectivness *= 0

    if atk_type == "POISON":
        if def_type1 == "GRASS" or def_type2 == "GRASS":
            total_effectivness *= 2
        if def_type1 == "POISON" or def_type2 == "POISON":
            total_effectivness *= 0.5
        if def_type1 == "GROUND" or def_type2 == "GROUND":
            total_effectivness *= 0.5
        if def_type1 == "BUG" or def_type2 == "BUG":
            total_effectivness *= 2
        if def_type1 == "ROCK" or def_type2 == "ROCK":
            total_effectivness *= 0.5
        if def_type1 == "GHOST" or def_type2 == "GHOST":
            total_effectivness *= 0.5

    if atk_type == "GROUND":
        if def_type1 == "FIRE" or def_type2 == "FIRE":
            total_effectivness *= 2
        if def_type1 == "ELECTRIC" or def_type2 == "ELECTRIC":
            total_effectivness *= 2
        if def_type1 == "GRASS" or def_type2 == "GRASS":
            total_effectivness *= 0.5
        if def_type1 == "POISON" or def_type2 == "POISON":
            total_effectivness *= 2
        if def_type1 == "FLYING" or def_type2 == "FLYING":
            total_effectivness *= 0
        if def_type1 == "BUG" or def_type2 == "BUG":
            total_effectivness *= 0.5
        if def_type1 == "ROCK" or def_type2 == "ROCK":
            total_effectivness *= 2

    if atk_type == "FLYING":
        if def_type1 == "ELECTRIC" or def_type2 == "ELECTRIC":
            total_effectivness *= 0.5
        if def_type1 == "GRASS" or def_type2 == "GRASS":
            total_effectivness *= 2
        if def_type1 == "FIGHTING" or def_type2 == "FIGHTING":
            total_effectivness *= 2
        if def_type1 == "BUG" or def_type2 == "BUG":
            total_effectivness *= 0.5
        if def_type1 == "ROCK" or def_type2 == "ROCK":
            total_effectivness *= 2

    if atk_type == "PSYCHIC":
        if def_type1 == "FIGHTING" or def_type2 == "FIGHTING":
            total_effectivness *= 2
        if def_type1 == "POISON" or def_type2 == "POISON":
            total_effectivness *= 2
        if def_type1 == "PSYCHIC" or def_type2 == "PSYCHIC":
            total_effectivness *= 0.5

    if atk_type == "BUG":
        if def_type1 == "FIRE" or def_type2 == "FIRE":
            total_effectivness *= 0.5
        if def_type1 == "GRASS" or def_type2 == "GRASS":
            total_effectivness *= 2
        if def_type1 == "FIGHTING" or def_type2 == "FIGHTING":
            total_effectivness *= 0.5
        if def_type1 == "POISON" or def_type2 == "POISON":
            total_effectivness *= 2
        if def_type1 == "FLYING" or def_type2 == "FLYING":
            total_effectivness *= 0.5
        if def_type1 == "PSYCHIC" or def_type2 == "PSYCHIC":
            total_effectivness *= 2
        if def_type1 == "GHOST" or def_type2 == "GHOST":
            total_effectivness *= 0.5

    if atk_type == "ROCK":
        if def_type1 == "FIRE" or def_type2 == "FIRE":
            total_effectivness *= 2
        if def_type1 == "ICE" or def_type2 == "ICE":
            total_effectivness *= 2
        if def_type1 == "FIGHTING" or def_type2 == "FIGHTING":
            total_effectivness *= 0.5
        if def_type1 == "GROUND" or def_type2 == "GROUND":
            total_effectivness *= 0.5
        if def_type1 == "FLYING" or def_type2 == "FLYING":
            total_effectivness *= 2
        if def_type1 == "BUG" or def_type2 == "BUG":
            total_effectivness *= 2

    if atk_type == "GHOST":
        if def_type1 == "NORMAL" or def_type2 == "NORMAL":
            total_effectivness *= 0
        if def_type1 == "PSYCHIC" or def_type2 == "PSYCHIC":
            total_effectivness *= 0
        if def_type1 == "GHOST" or def_type2 == "GHOST":
            total_effectivness *= 2

    if atk_type == "DRAGON":
        if def_type1 == "DRAGON" or def_type2 == "DRAGON":
            total_effectivness *= 2

    # RETURN A FLOAT TO MULTIPLY THE DAMAGE
    return total_effectivness
