def slugify(s):
    return s.strip().lower().replace(" ", "_").replace("-", "_")


def main():
    print(slugify(input("Enter program title: ")))


if __name__ == "__main__":
    main()
