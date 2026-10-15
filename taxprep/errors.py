"""Stable errors shared by the command and storage layers."""


class AppError(Exception):
    def __init__(self, code, message, exit_code=2, details=None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.exit_code = exit_code
        self.details = details
