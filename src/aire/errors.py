class AIREError(Exception):

    def __init__(
        self,
        reason: str,
        underlying_error: Exception | None = None,
    ):
        self.reason = reason
        self.underlying_error = underlying_error

        super().__init__()

    def __repr__(self) -> str:
        return f"{self.reason} ({self.underlying_error})"

    def __str__(self) -> str:
        return self.__repr__()
