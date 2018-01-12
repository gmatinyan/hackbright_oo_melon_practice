############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    code = None
    first_harvest = None
    color = None
    is_seedless = None
    is_bestseller = None
    name = None
    pairings = []

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'casaba')
    casaba.add_pairing(['strawberries', 'mint'])
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True,
                                  'yellow watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)
    # Fill in the rest

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # melon_types = make_melon_types()

    # Fill in the rest
    for melon in melon_types:
        print "{name} pairs with:".format(name=melon.name)

        for pairing in melon.pairings:
            print "- {pairing}".format(pairing=pairing)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

    reporting_codes = {}

    for melon in melon_types:
        reporting_codes[melon.code] = melon

    return reporting_codes

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    melon_type = None
    shape_rating = None
    color_rating = None
    field = None
    harvester = None
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(melon):
        """Checks if a melon is sellable. Returns a boolean."""

        if melon.field != 3:
            if melon.shape_rating > 5 and melon.color_rating > 5:
                return True

        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_melon_types = []

    melon1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    all_melon_types.append(melon1)

    melon2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila')
    all_melon_types.append(melon2)

    melon3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila')
    all_melon_types.append(melon3)

    melon4 = Melon(melon_types['cas'], 10, 6, 35, 'Sheila')
    all_melon_types.append(melon4)

    melon5 = Melon(melon_types['cren'], 8, 9, 35, 'Michael')
    all_melon_types.append(melon5)

    melon6 = Melon(melon_types['cren'], 8, 2, 35, 'Michael')
    all_melon_types.append(melon6)

    melon7 = Melon(melon_types['cren'], 2, 3, 4, 'Michael')
    all_melon_types.append(melon7)

    melon8 = Melon(melon_types['cren'], 6, 7, 4, 'Michael')
    all_melon_types.append(melon8)

    melon9 = Melon(melon_types['yw'], 7, 10, 3, 'Sheila')
    all_melon_types.append(melon9)

    # Fill in the rest

    return all_melon_types


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    melon_num = 1
    # Fill in the rest
    for melon in melons:
        print """Melon {num}
        - Melon type: {melon_type}
        - Shape rating: {shape_rating}
        - Color rating: {color_rating}
        - Harvested from field {field_num}
        - Harvested by {harvester}
        """.format(num=melon_num, melon_type=melon.melon_type.code,
                   shape_rating=melon.shape_rating,
                   color_rating=melon.color_rating, field_num=melon.field,
                   harvester=melon.harvester)
        melon_num += 1

        if melon.is_sellable():
            print "Ready to sell.\n"
        else:
            print "DO NOT SELL, NOT SAFE FOR CONSUMPTION.\n"

melon_types = make_melon_types()
melon_types = make_melon_type_lookup(melon_types)
melons = make_melons(melon_types)
melon_report = get_sellability_report(melons)
