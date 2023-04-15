class ValidationError(Exception):
    """The django validation error works with a list of errors, but we want to
    work with a single error, so we create a new exception to handle this
    """

    pass
