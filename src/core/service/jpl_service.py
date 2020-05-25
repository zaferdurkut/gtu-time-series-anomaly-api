from src.infra.client.jpl.jpl import JPLClient


if __name__ == '__main__':
    result = JPLClient.get_data("ATW2")

    print(result)
