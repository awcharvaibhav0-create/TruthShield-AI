def verify_source(source):

    trusted_sources = [
        "BBC",
        "Reuters",
        "Associated Press",
        "WHO",
        "United Nations"
    ]

    if not source:
        return {
            "source": "Unknown",
            "score": 50
        }

    if source in trusted_sources:
        return {
            "source": source,
            "score": 90
        }

    return {
        "source": source,
        "score": 40
    }