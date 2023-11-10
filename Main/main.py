from PySide2.QtWidgets import QApplication
from Designs.de_sandbox import SandBox
from Designs.de_main_window import MainWindow


def run_program():
    app_session = QApplication()  # Need to pass app_session to Main_window so it won't disappear

    mw = MainWindow(app_session)
    mw.setup_ui()
    mw.setSandbox(SandBox(mw))
    mw.sandbox.add_rect(1,2,3,4)

    mw.show()

    app_session.exec_()


if __name__ == '__main__':
    run_program()
