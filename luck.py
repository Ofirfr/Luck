
import random
NUM_OF_PEOPLE = 10, 000
PERCENTAGE_WEIGHT_OF_LUCK = 5
NUM_OF_ITERATIONS = 100


def main():

    # Calculate the weight of luck and skill
    weight_of_luck = PERCENTAGE_WEIGHT_OF_LUCK / 100
    weight_of_skill = 1 - weight_of_luck
    print("Luck accounts for {}% and skill accounts for {}%".format(
        weight_of_luck * 100, weight_of_skill * 100))

    # Generate the statistics based on random luck and skill
    all_stats = []
    for j in range(NUM_OF_ITERATIONS):
        batch = []
        for j in range(NUM_OF_PEOPLE):
            id = j
            luck = random.randint(0, 100) * weight_of_luck
            skill = random.randint(0, 100) * weight_of_skill
            total_chance = luck + skill
            stat_line = {"id": id, "luck": luck,
                         "skill": skill, "total": total_chance}
            batch.append(stat_line)

        # Get best 10 by total
        batch.sort(key=lambda x: x["total"], reverse=True)
        top_10_by_total = set(batch[0:10])
        # Calculate the average luck and skill
        average_luck = sum([x["luck"] for x in top_10_by_total]) / 10
        average_skill = sum([x["skill"] for x in top_10_by_total]) / 10
        # Get best 10 by skill
        batch.sort(key=lambda x: x["skill"], reverse=True)
        top_10_by_skill = set(batch[0:10])
        # Appear in both
        both_by_total_and_skill = top_10_by_total.intersection(
            top_10_by_skill
        )
        batch_stat_line = {
            "total": top_10_by_total, "skill": top_10_by_skill, "both": both_by_total_and_skill,
            "average_luck": average_luck, "average_skill": average_skill
        }
        all_stats.append(batch_stat_line)

    # Print the results


if __name__ == "__main__":
    main()
