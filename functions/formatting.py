def describe_result(change: int) -> tuple[str, str]:
    if change > 0:
        return f"Jackpot ! +{change} Points", "#4CAF50"
    if change < 0:
        return f"Poor Player... {change} points", "#F44336"
    return "Sorry... Try Again !", "gray"
