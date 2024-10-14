import UIController

class Automated_WI_generator:
    def __init__(self) -> None:
        main_window = UIController.App()
        main_window.run_app()

def main() -> None:
    Automated_WI_generator()

if __name__ == '__main__':
    main()