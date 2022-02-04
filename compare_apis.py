import requests
import datetime

def fetch_data_rest(with_comment=True):
    start = datetime.datetime.now()

    response = requests.get(
        "http://localhost:5000/rest/blog",
        params={"comments": with_comment}
    )
    data = response.json()
    end = datetime.datetime.now()

    return end - start

def fetch_data_rest_title():
    start = datetime.datetime.now()

    response = requests.get("http://localhost:5000/rest/blog-title")
    data = response.json()
    end = datetime.datetime.now()

    return end - start

def fetch_data_rest_text():
    start = datetime.datetime.now()

    response = requests.get("http://localhost:5000/rest/blog-text")
    data = response.json()
    end = datetime.datetime.now()

    return end - start


def fetch_data_graphql(with_comment=True):
    start = datetime.datetime.now()

    if with_comment:
        query = """query {
            posts{
                id
                title
                intro
                subtitle1
                subtext1
                subtitle2
                subtext2
                subtitle3
                subtext3
                subtitle4
                subtext4
                subtitle5
                subtext5
                conclusion
                createdAt
                user{
                    egdes{
                        node{
                            username
                        }
                    }
                }
                category{
                    egdes{
                        node{
                            username
                        }
                    }
                }
                comments{
                    edges{
                        node{
                            id
                            text
                            createdAT
                        }
                    }
                }
            }
        }""".format(user_id)
    else:
        query = """query {
            posts{
                id
                title
                intro
                subtitle1
                subtext1
                subtitle2
                subtext2
                subtitle3
                subtext3
                subtitle4
                subtext4
                subtitle5
                subtext5
                conclusion
                createdAt
                user{
                    egdes{
                        node{
                            username
                        }
                    }
                }
                category{
                    egdes{
                        node{
                            username
                        }
                    }
                }
            }
        }"""

    response = requests.post(
        "http://localhost:5000/graphql",
        json={"query": query}
    )
    data = json.loads(response.text)["data"]

    end = datetime.datetime.now()

    return end - start

def fetch_data_graphql_title():
    start = datetime.datetime.now()

    query = """query {
        posts{
            id
            title
            intro
            subtitle1
            subtitle2
            subtitle3
            subtitle4
            subtitle5
        }
    }"""

    response = requests.post(
       "http://localhost:5000/graphql",
        json={"query": query}
    )
    data = json.loads(response.text)["data"]

    end = datetime.datetime.now()

    return end - start

def fetch_data_graphql_text():
    start = datetime.datetime.now()

    query = """query {
        posts{
            id
            subtext1
            subtext2
            subtext3
            subtext4
            subtext5
            conclusion
        }
    }"""

    response = requests.post(
        "http://localhost:5000/graphql",
        json={"query": query}
    )
    data = json.loads(response.text)["data"]

    end = datetime.datetime.now()

    return end - start


def get_times():
    result = {}

    result["REST_WITH_COMMENT"] = fetch_data_rest(True)
    result["REST_WITHOUT_COMMENT"] = fetch_data_rest(False)
    result["GRAPHQL_WITH_COMMENT"] = fetch_data_graphql(True)
    result["GRAPHQL_WITHOUT_COMMENT"] = fetch_data_graphql(False)
    result["REST_TITLE"] = fetch_data_rest_title()
    result["REST_TEXT"] = fetch_data_rest_text()
    result["GRAPHQL_TITLE"] = fetch_data_graphql_title()
    result["GRAPHQL_TEXT"] = fetch_data_graphql_text()

    return result

def main():
    data = get_times()

    print(f"the data are: ", data)

if __name__ == "__main__":
    main()
