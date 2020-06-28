from Utils import SCORES_FILE_NAME
import Live


def add_score(difficulty):
    try:
        with open(f"{SCORES_FILE_NAME}", mode='r', encoding='utf-8') as f:
            current_score = f.read()
            # print(current_score, type(current_score))
            point_of_winning = int(difficulty) * 3 + 5
            f = open(f"{SCORES_FILE_NAME}", mode='w', encoding='utf-8')
            f.write(str(point_of_winning+int(current_score)))

    except IOError:
        with open("Scores.txt", "wt") as out_file:
            point_of_winning = int(difficulty) * 3 + 5
            out_file.write(str(point_of_winning))

    finally:
        f.close()
    return point_of_winning




