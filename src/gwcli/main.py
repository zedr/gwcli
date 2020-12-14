from gwcli.manager import Manager

def main():
    print(list(Manager.get_mount_paths()))

if __name__ == "__main__":
    main()
