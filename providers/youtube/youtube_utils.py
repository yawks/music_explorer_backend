from datetime import datetime


def convert_duration(duration: str) -> int:
    """Convert the string duration into number of seconds

    Args:
        duration (str): duration in HH:MM:SS or MM:SS

    Returns:
        int: the number of seconds of the duration
    """
    duration_in_sec: int = 0
    if duration.isnumeric():
        duration_in_sec = int(duration)
    elif duration.count(":") == 1:
        duration_in_sec = int((datetime.strptime(
            duration, "%M:%S")-datetime(1900, 1, 1)).total_seconds())
    elif duration.count(":") == 2:
        duration_in_sec = int((datetime.strptime(
            duration, "%H:%M:%S")-datetime(1900, 1, 1)).total_seconds())

    return duration_in_sec
