def get_overtime_application_minutes(start_time, end_time) -> int:
    difference = end_time - start_time
    minutes = difference.seconds//60
    seconds = difference.seconds%60
    return minutes + (seconds/60) 