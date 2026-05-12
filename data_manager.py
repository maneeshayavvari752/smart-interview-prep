def generate_schedule(hours):
    hours = int(hours)

    schedule = []

    if hours == 1:
        schedule = [
            "Learn one concept"
        ]

    elif hours == 2:
        schedule = [
            "Learn concepts",
            "Solve problems"
        ]

    elif hours == 3:
        schedule = [
            "Learn concepts",
            "Solve practice problems",
            "Revision"
        ]

    elif hours == 4:
        schedule = [
            "Learn concepts",
            "Solve easy problems",
            "Solve medium problems",
            "Revision"
        ]

    else:
        schedule = [
            "Learn concepts",
            "Solve easy problems",
            "Solve medium problems",
            "Solve hard problems",
            "Revision"
        ]

    return schedule