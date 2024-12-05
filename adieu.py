def format_names(names: list)-> str:
    no_names: int = len(names)
    if no_names == 1:
        return "{}".format(*names)
    elif no_names == 2:
        return "{} and {}".format(*names)
    else:
        return "{}, and {}".format(", ".join(names[:-1]), names[-1])
def main()-> None:
    names = []
    while True:
        try:
            name: str = input("Name: ")
        except EOFError:
            print(f"\nAdieu, adieu, to {format_names(names)}")
            return
        else:
            names.append(name)
if __name__ == "__main__":
    main()