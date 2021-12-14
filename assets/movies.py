class MovieScore:

    def __init__(self, value, lower=0, upper=100):
        for param in [value, lower, upper]:
            if not isinstance(param, int):
                raise TypeError("All params must be ints.")
        if not lower <= value <= upper:
            raise ValueError(f"A MovieScore must be an int between {lower} and {upper}.")
        self.__value = value
        if lower >= upper:
            raise ValueError(
                "The lower bound must be lower than the upper bound."
            )
        self.__lower = lower
        self.__upper = upper

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_val):
        if not isinstance(new_val, int):
            raise TypeError("Must be an int.")
        if not self.lower <= new_val <= self.upper:
            raise ValueError(
                f"Must be an int between the lower bound and upper bound."
                f"\n\tLower Bound: {self.lower}"
                f"\n\t Upper Bound: {self.upper}"
            )
        self.__value = new_val

    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an int")
        if value >= self.upper:
            raise ValueError(
                f"Lower bound must be less than upper bound.\n\tLower Bound: {value}\n\tUpper Bound: {self.upper}"
            )
        self.__lower = value

    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an int")
        if value <= self.lower:
            raise ValueError(
                f"Lower bound must be less than upper bound.\n\tLower Bound: {self.lower}\n\tUpper Bound: {value}"
            )
        self.__upper = value


class Movie:

    def __init__(self, title, year, my_rating, director, rottom, imdb):
        # Mutable
        self.my_rating = MovieScore(my_rating)
        self.rottom = MovieScore(rottom)
        self.imdb = MovieScore(imdb)

        # Frozen
        if not isinstance(year, int):
            raise TypeError("Years are expected as ints. I.E: 1999")
        self.__year = year
        for param in [title, director]:
            if not isinstance(param, str):
                raise TypeError("The title and Director should be strings.")
        self.__title = title
        self.__director = director

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        raise AttributeError("Titles cannot be altered.")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        raise AttributeError("Years cannot be altered.")

    @property
    def director(self):
        return self.__title

    @director.setter
    def director(self, value):
        raise AttributeError("Directors cannot be altered.")


