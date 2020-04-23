def convert_result_to_message(result):
    if len(result) == 0:
        print("😞")

    content = []

    for data in result:
        message = ""
        message += f"Profile: {data['name']}\n"
        message += f"Company: {data['company']}\n"
        message += f"Job Posted: {data['date_posted']}\n"
        message += "Requirement\n"
        count = 1
        for step in data['requirement']:
            message += f"{count}. {step}\n"
            count += 1
        message += '\n'
        message += f"{data['link']}\n\n"
        content.append(message)

    return content