# usage:
# > unzip submits.zip
# > python3 prepare.py submits 38048
import os
import shutil
import argparse
import pathlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=pathlib.Path)
    parser.add_argument('output', type=pathlib.Path)
    args = parser.parse_args()

    participants = os.listdir(args.input)

    os.mkdir(args.output)

    for participant in participants:
        if participant == args.output:
            continue
        if os.path.isdir(os.path.join(args.input, participant)):
            added_problems = set()
            for submit in os.listdir(os.path.join(args.input, participant)):
                prob = submit.split('-')[0]

                if not os.path.exists(os.path.join(args.output, prob)):
                    os.makedirs(os.path.join(args.output, prob))

                if prob not in added_problems and "OK" in submit:
                    new_submit = submit
                    if "clang" in new_submit:
                        new_submit += ".cpp"
                    added_problems.add(prob)
                    shutil.copy(os.path.join(args.input, participant, submit), os.path.join(args.output, prob, new_submit))
