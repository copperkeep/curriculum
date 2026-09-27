def domains(emails):
    return {e.split("@")[1] for e in emails}
