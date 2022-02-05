import requests
import datetime
import time

import matplotlib.pyplot as plt

def fetch_data_rest(with_comment=True):
    start = time.time()

    response = requests.get(
        "http://localhost:5000/rest/blog",
        params={"comments": with_comment}
    )
    # data = response.json()
    end = time.time()

    return end - start

def fetch_data_rest_title():
    start = time.time()

    response = requests.get("http://localhost:5000/rest/blog-title")
    #data = response.json()
    end = time.time()

    return end - start

def fetch_data_rest_text():
    start = time.time()

    response = requests.get("http://localhost:5000/rest/blog-text")
    #data = response.json()
    end = time.time()

    return end - start


def fetch_data_graphql(with_comment=True):
    start = time.time()

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
                    username
                }
                category{
                    id
                    name
                    description
                }
                comments{
                    edges{
                        node{
                            id
                            text
                            createdAt
                        }
                    }
                }
            }
        }"""
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
                    username
                }
                category{
                    id
                    name
                    description
                }
            }
        }"""

    response = requests.post(
        "http://localhost:5000/graphql",
        json={"query": query}
    )
    #data = json.loads(response.text)["data"]

    end = time.time()

    return end - start

def fetch_data_graphql_title():
    start = time.time()

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
    #data = json.loads(response.text)["data"]

    end = time.time()

    return end - start

def fetch_data_graphql_text():
    start = time.time()

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
    #data = json.loads(response.text)["data"]

    end = time.time()

    return end - start


def get_times():
    result = {}

    result["REST_WITH_COMMENT"] = fetch_data_rest(True)
    result["GRAPHQL_WITH_COMMENT"] = fetch_data_graphql(True)
    result["REST_WITHOUT_COMMENT"] = fetch_data_rest(False)
    result["GRAPHQL_WITHOUT_COMMENT"] = fetch_data_graphql(False)
    result["REST_TITLE"] = fetch_data_rest_title()
    result["GRAPHQL_TITLE"] = fetch_data_graphql_title()
    result["REST_TEXT"] = fetch_data_rest_text()
    result["GRAPHQL_TEXT"] = fetch_data_graphql_text()

    return result

def save_result_as_png(data):
    names = list(data.keys())
    values = list(data.values())

    pos = range(len(names))
    l = ["blue", "orange", "green", "red", "purple", "cyan", "olive", "gray"]

    plt.bar(names, values, color=l)
    # plt.xticks(pos, names)
    plt.xlabel("Differents Experiences", fontsize=12)
    plt.ylabel("Times in s")
    plt.title("Result of the experience")
    plt.legend(names)
    plt.savefig('result.png') 


def main():
    print("-----------Start Exp--------------")
    data = get_times()
    print(f"the data are: ", data)
    save_result_as_png(data)
    print("-----------Exp Done--------------")

if __name__ == "__main__":
    main()
