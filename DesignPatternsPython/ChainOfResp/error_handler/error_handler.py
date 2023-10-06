# Handler interface
class ErrorHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_error(self, error_type, message):
        if self.successor:
            self.successor.handle_error(error_type, message)
        else:
            print(f"Unhandled Error: {error_type} - {message}")

# Concrete Handlers
class FileErrorHandler(ErrorHandler):
    def handle_error(self, error_type, message):
        if error_type == "FileError":
            print(f"Logging File Error: {message}")
        else:
            super().handle_error(error_type, message)

class DatabaseErrorHandler(ErrorHandler):
    def handle_error(self, error_type, message):
        if error_type == "DatabaseError":
            print(f"Logging Database Error: {message}")
        else:
            super().handle_error(error_type, message)

class GeneralErrorHandler(ErrorHandler):
    def handle_error(self, error_type, message):
        print(f"Logging General Error: {error_type} - {message}")

# Client
class ErrorLogger:
    def __init__(self):
        self.error_handler_chain = FileErrorHandler(DatabaseErrorHandler(GeneralErrorHandler()))

    def log_error(self, error_type, message):
        self.error_handler_chain.handle_error(error_type, message)

# Example usage
logger = ErrorLogger()
logger.log_error("FileError", "File not found")
logger.log_error("DatabaseError", "Connection error")
logger.log_error("ValidationError", "Invalid input")
