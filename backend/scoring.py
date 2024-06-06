def score_inclusivity(content):
    scores = {
        'Youth Representation': 1 if 'youth' in content else 0,
        # Add other criteria checks here
    }
    total_score = sum(scores.values())
    return total_score
