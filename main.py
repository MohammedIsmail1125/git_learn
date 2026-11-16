def compare_deadlines(earlier, revised):
    if earlier == revised:
        return "Deadline unchanged"

    return f"Deadline changed from {earlier} to {revised}"


print(compare_deadlines("20 Nov, 4 PM", "21 Nov, 12 PM"))