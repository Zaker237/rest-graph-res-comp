import requests
import datetime

REST_API_ENDPOINT = "http://localhost:5000/rest/blog"
GRAPHQL_API_ENDPOINT = "http://localhost:5000/graphql"

def fetch_data_rest(with_comment=True):
    start = datetime.datetime.now()

    response = requests.get(REST_API_ENDPOINT)
    data = response.json()
    end = datetime.datetime.now()

    return end - start


def fetch_data_graphql(with_comment=True):
    start = datetime.datetime.now()

    if with_comment:
        query = """query {
            post(user: '{}'){
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
            post(user: '{}'){
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
        }""".format(user_id)

    response = requests.post(
        GRAPHQL_API_ENDPOINT,
        json={"query": query}
    )
    data = json.loads(response.text)["data"]

    end = datetime.datetime.now()

    return end - start

def fetch_data_graphql_title():
    start = datetime.datetime.now()

    query = """query {
        post(user: '{}'){
            id
            title
            intro
            subtitle1
            subtitle2
            subtitle3
            subtitle4
            subtitle5
        }
    }""".format(user_id)

    response = requests.post(
        GRAPHQL_API_ENDPOINT,
        json={"query": query}
    )
    data = json.loads(response.text)["data"]

    end = datetime.datetime.now()

    return end - start

def fetch_data_graphql_title():
    start = datetime.datetime.now()

    query = """query {
        post(user: '{}'){
            id
            subtext1
            subtext2
            subtext3
            subtext4
            subtext5
            conclusion
        }
    }""".format(user_id)

    response = requests.post(
        GRAPHQL_API_ENDPOINT,
        json={"query": query}
    )
    data = json.loads(response.text)["data"]

    end = datetime.datetime.now()

    return end - start


def main():
    pass

if __name__:
    main()
