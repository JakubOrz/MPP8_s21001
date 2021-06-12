import sys
import os
from Biblioteki import Core


def main3(*args) -> None:
    def print_welcome_message():
        options = {"-d --decode": "Na podstawie kodu uzyskanego z plik_z_probka_jezyka wyświetla"
                                  "odkodowane zawartości plików",
                   "-h --help": "Wyświetla instrucje",
                   "-s --save": "Wynik operacji zostaje zapisany do pliku Results/<encoded|decoded>filename.txt",
                   }

        print(f"Witam w moim prostym dekoderze Huffmana tym razem bez interejsu graficznego\n"
              f"Używanie:python3 mpp8_s21001.py [opcje] <plik_z_probka_jezyka> <pliki_do_zakodowania>... \n"
              f"\nOpcje:")
        for option in options.keys():
            print(f"{option} : {options.get(option)}")

    if len(args[0]) <= 1 or "-h" in args[0] or "--help" in args[0]:
        print_welcome_message()
        return

    encode_flag = True
    to_file_flag = False
    arg_ignored = 0

    if "-d" in args[0] or "--decode" in args[0]:
        encode_flag = False
        arg_ignored += 1

    if "-s" in args[0] or "--save" in args[0]:
        to_file_flag = True
        if not os.path.exists("Results"):
            os.makedirs("Results")
        arg_ignored += 1

    try:
        coding = Core.huffman_encode(Core.prepare_chars(args[0][1 + arg_ignored]))
    except FileNotFoundError:
        print(f"Nie można odczytać pliku z próbką języka")
        return

    for file_to_process in args[0][2 + arg_ignored:]:
        proceed = Core.deal_with_file(file_path=file_to_process, coding=coding, encode=encode_flag)
        if to_file_flag:
            with open("Results/"+("encoded" if encode_flag else "decoded")+"_"+file_to_process.replace("/", ""), 'w') \
                    as resultfile:
                resultfile.write(proceed)
        else:
            print(f"{file_to_process} -> {proceed}")


if __name__ == '__main__':
    main3(sys.argv)
