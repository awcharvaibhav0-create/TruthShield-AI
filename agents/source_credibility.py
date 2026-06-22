def source_credibility(source):

    trusted_sources = {
        "Reuters": 95,
        "BBC": 90,
        "Associated Press": 95,
        "AP": 95,
        "WHO": 98,
        "NASA": 99,
        "UN": 95,
        "The Hindu": 85,
        "Indian Express": 85
    }

    source = source.strip()

    if source in trusted_sources:
        return trusted_sources[source]

    return 50