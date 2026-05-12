from questions import QUESTION_BANK, COMPANY_FOCUS


def recommend_questions(weak_topics):
    recommendations = []

    for topic in weak_topics:
        topic = topic.strip()

        if topic.lower() == "dp":
            topic = "DP"
        else:
            topic = topic.title()

        if topic in QUESTION_BANK:
            for question in QUESTION_BANK[topic]:
                recommendations.append(question)

    return recommendations


def get_company_focus(company):
    company = company.title()

    if company in COMPANY_FOCUS:
        return COMPANY_FOCUS[company]

    return ["General DSA Practice"]