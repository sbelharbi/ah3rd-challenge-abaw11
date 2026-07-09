import os
import sys
from os.path import dirname, abspath, join, basename, expanduser, normpath


root_dir = dirname((abspath(__file__)))
sys.path.append(root_dir)

def load_content(path: str) -> list:
    assert os.path.isfile(path), path
    with open(path, 'r') as fx:
        content = fx.readlines()

    out = []
    for l in content:
        l = l.strip()
        out.append(l)

    return out


def validate_with_probabilities(submission_path: str) -> bool:
    ref_path = join(root_dir,
                    'predictions-submissions/with_probabilities/trial-0.txt')
    ref_cont = load_content(ref_path)
    sub_cont = load_content(submission_path)

    n_r = len(ref_cont)
    n_s = len(sub_cont)
    assert n_r == n_s, f"Number of videos does match. {n_r} | {n_s}"

    for item_r, item_s in zip(ref_cont, sub_cont):
        # line format: video-id,p0,p1,prd
        parts_r = item_r.split(',')
        parts_s = item_s.split(',')
        assert len(parts_r) == len(parts_s), f"Mismatch of number of items"
        assert len(parts_s) == 4, f"{len(item_s)}"

        assert item_r[0] == item_s[0], "Mismatch of video id"
        p0 = float(parts_s[1])
        p1 = float(parts_s[2])
        assert 0. <= p0 <= 1., f"{parts_s[0]}: {p0}"
        assert 0. <= p1 <= 1., f"{parts_s[0]}: {p1}"
        assert (p0 + p1) == 1., f"{parts_s[0]}: {p0 + p1}"

        prd = int(parts_s[3])
        assert prd in [0, 1], f"{parts_s[0]}: {prd}"

    print(f"The submission {submission_path} is valid.")

    return True


def validate_without_probabilities(submission_path: str) -> bool:
    ref_path = join(root_dir,
                    'predictions-submissions/no_probabilities/trial-0.txt')
    ref_cont = load_content(ref_path)
    sub_cont = load_content(submission_path)

    n_r = len(ref_cont)
    n_s = len(sub_cont)
    assert n_r == n_s, f"Number of videos does match. {n_r} | {n_s}"

    for item_r, item_s in zip(ref_cont, sub_cont):
        # line format: video-id,prd
        parts_r = item_r.split(',')
        parts_s = item_s.split(',')
        assert len(parts_r) == len(parts_s), f"Mismatch of number of items"
        assert len(parts_s) == 2, f"{len(item_s)}"

        assert parts_r[0] == parts_s[0], "Mismatch of video id"
        prd = int(parts_s[1])
        assert prd in [0, 1], f"{parts_s[0]}: {prd}"

    print(f"The submission {submission_path} is valid.")

    return True


if __name__ == "__main__":
    your_submission_trial_path = ''
    # uncomment one of the following depending on your case
    # validate_without_probabilities(your_submission_trial_path)
    # validate_with_probabilities(your_submission_trial_path)
