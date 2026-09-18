def process_payment():
    """Convert a low-level connection error into a useful application error."""
    try:
        # Imagine the payment system failed.
        raise ConnectionError("Payment server is not responding")
    except ConnectionError as e:
        # "from e" preserves the original error as the cause.
        raise ValueError("Payment could not be completed") from e


try:
    process_payment()
except ValueError as e:
    print("Order failed:", e)


def get_port():
    """Read and validate the port number from the configuration file."""
    try:
        with open("config.txt") as file:
            return int(file.read())
    except FileNotFoundError as e:
        raise ValueError("Application configuration is missing") from e
    except ValueError as e:
        raise ValueError("Port number in config.txt is invalid") from e

    # from e ---> keep the connection to the origional error."I got this new error because of the old error."
    # from None --->"Show my new error, but don't show the original error."Hide the original error's context.