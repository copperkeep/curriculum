from datetime import date, timedelta

def schedule(start_iso, weeks):
    start = date.fromisoformat(start_iso)
    return [(start + timedelta(weeks=i)).strftime("%a %d %b") for i in range(weeks)]
