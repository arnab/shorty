import httpagentparser

def parse_browser(user_agent_string):
    browser = httpagentparser.detect(user_agent_string)
    return [
        browser['os']['name'],
        browser['browser']['name'],
        browser['browser']['version'],
    ]
