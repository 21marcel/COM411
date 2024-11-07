# observations = {"Car", "Sky Scraper", "House", "House", "Sky Scraper", "Bike"}
# print(observations)


def observed_items():
    observations = []

    for i in range (7):
        print("Please enter an observation")
        observation = input()
        observations.append(observation)

    return observations

def run_task2():
    print("Counting observations...")

    observations = observed_items()
    obs_counts = set()
    for item in observations:
        obs=(item, observations.count(item))
        obs_counts.add(obs)
    print(obs_counts)


run_task2()

def observing_items():
    observed = []

    for i in range (5):
        print("Please enter an observation")

