import re

errors = 0

def detranslated(value):

    value = value + ')))' if errors > 3 else value

    print(value)


pattern = {

    r'spam':'print exit',
    r'exit':'print spam',

}

while True:

    a = input('\nexit?: ').lower()

    n1 = 0

    try:

        while True:

            keyApp = list(pattern.keys())[n1]
            valueApp = list(pattern.values())[n1]
            match = re.search(keyApp, a)

            if not match:

                n1 += 1

            else:

                if match:

                    if match.start() <= 5:

                        errors += 1
                        detranslated(valueApp); break

                    else:

                        print('I don\'t understand you!'); break


    except IndexError:
       print('NONONONO, spam or exit!')