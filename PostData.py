class PostData:
    title = ""
    owner = ""
    type = ""
    description = ""
    steps = ""
    ingredients = ""
    prep_Time = 0

    def __init__(self, t, own, typ, d, step, ingr, prep):
        self.title = t
        self.owner = own
        self.type = typ
        self.description = d
        self.steps = step
        self.ingredients = ingr
        self.prep_Time = prep
