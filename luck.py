import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

NUM_OF_PEOPLE = 1000
PERCENTAGE_WEIGHT_OF_LUCK = 5
NUM_OF_ITERATIONS = 1000


def main():

    # Calculate the weight of luck and skill
    weight_of_luck = PERCENTAGE_WEIGHT_OF_LUCK / 100
    weight_of_skill = 1 - weight_of_luck
    print("Luck accounts for {}% and skill accounts for {}%".format(
        weight_of_luck * 100, weight_of_skill * 100))

    # Generate the statistics based on random luck and skill
    all_stats = []
    total_luck_sum = 0
    total_skill_sum = 0
    total_both_by_total_and_skill = 0

    for i in range(NUM_OF_ITERATIONS):
        batch = []
        for j in range(NUM_OF_PEOPLE):
            id = j
            luck = random.randint(0, 100)
            luck_with_weight = luck * weight_of_luck
            skill = random.randint(0, 100)
            skill_with_weight = skill * weight_of_skill
            total_chance = luck_with_weight + skill_with_weight
            stat_line = {"id": id, "luck": luck,
                         "skill": skill, "total": total_chance}
            batch.append(stat_line)

        # Get best 10 by total
        batch.sort(key=lambda x: x["total"], reverse=True)
        top_10_by_total = batch[0:10]

        # Calculate the average luck and skill for this iteration
        average_luck = sum([x["luck"] for x in top_10_by_total]) / 10
        average_skill = sum([x["skill"] for x in top_10_by_total]) / 10

        # Add to the total luck and skill sums for overall average calculation
        total_luck_sum += average_luck
        total_skill_sum += average_skill

        # Get best 10 by skill
        batch.sort(key=lambda x: x["skill"], reverse=True)
        top_10_by_skill = batch[0:10]

        # Appear in both by comparing their ids
        both_by_total_and_skill = [person for person in top_10_by_total if person["id"] in [
            x["id"] for x in top_10_by_skill]]
        total_both_by_total_and_skill += len(both_by_total_and_skill)

        batch_stat_line = {
            "total": top_10_by_total,
            "skill": top_10_by_skill,
            "both": both_by_total_and_skill,
            "average_luck": average_luck,
            "average_skill": average_skill
        }
        all_stats.append(batch_stat_line)

    # Overall averages across all iterations
    overall_average_luck = total_luck_sum / NUM_OF_ITERATIONS
    overall_average_skill = total_skill_sum / NUM_OF_ITERATIONS
    overall_average_both_count = total_both_by_total_and_skill / NUM_OF_ITERATIONS

    print(f"Overall Average Luck: {overall_average_luck}")
    print(f"Overall Average Skill: {overall_average_skill}")
    print(
        f"Average Count of People in Both Top 10 by Total and Skill: {overall_average_both_count}")

    # Plot 1: Overall Average Luck vs Skill (displaying as numbers)
    plt.figure(figsize=(5, 3))
    plt.bar(["Average Luck", "Average Skill"], [overall_average_luck,
            overall_average_skill], color=['blue', 'green'])
    plt.title('Overall Average Luck vs Skill')
    plt.savefig('overall_average_luck_vs_skill.png')
    plt.close()

    # Plot 2: Average Count of People in Both Top 10 by Total and Skill
    plt.figure(figsize=(5, 3))
    plt.bar(["Average Count in Both"], [
            overall_average_both_count], color='purple')
    plt.title('Average Count of People in Both Top 10 by Total and Skill')
    plt.savefig('average_count_in_both_top_10.png')
    plt.close()

    # Plot 3: Distribution of Luck and Skill for Top 10 by Total in Last Iteration (Stacked Bar Chart)
    final_batch = all_stats[-1]["total"]
    final_luck = [x["luck"] for x in final_batch]
    final_skill = [x["skill"] for x in final_batch]
    indices = np.arange(len(final_luck))

    plt.figure(figsize=(10, 6))
    plt.bar(indices, final_luck, label='Luck',
            color='blue', bottom=final_skill)  # Stack Luck
    plt.bar(indices, final_skill, label='Skill',
            color='green')  # Stack Skill on top of Luck
    plt.xlabel('Top 10 People by Total (Last Iteration)')
    plt.ylabel('Value')
    plt.title('Distribution of Luck and Skill for Top 10 by Total (Last Iteration)')
    plt.legend()
    plt.savefig('distribution_of_luck_and_skill_stacked.png')
    plt.close()


if __name__ == "__main__":
    main()
