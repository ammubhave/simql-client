"""SimQL Execution Unit"""
from exceptions import ExitException


def execute(query):
    """Executes the SimQL query and returns a JSON result or None

    :param query: The SimQL query to execute
    :type query: str
    :returns: list of results or None if no result
    :raises: ExitException
    """
    if query == 'exit':
        raise ExitExeption()
