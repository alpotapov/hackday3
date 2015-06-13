import webbrowser
from figo import FigoConnection, FigoSession

connection = FigoConnection("CaESKmC8MAhNpDe5rvmWnSkRE_7pkkVIIgMwclgzGcQY", "STdzfv0GXtEj_bwYn7AgCVszN1kKq5BdgEIKOM_fzybQ", "https://radiant-cove-8704.herokuapp.com")


def start_login():
    # open the webbrowser to kick of the login process
    webbrowser.open(connection.login_url(scope="accounts=ro transactions=ro", state="qweqwe"))


def process_redirect(authentication_code, state):
    # handle the redirect url invocation, which gets passed an authentication code and the state (from the initial login_url call)

    # authenticate the call
    if state != "qweqwe":
        raise Exception("Bogus redirect, wrong state")

    # trade in authentication code for access token
    token_dict = connection.convert_authentication_code(authentication_code)

    # start session
    session = FigoSession(token_dict["access_token"])

    # access data
    for account in session.accounts:
        print account.name