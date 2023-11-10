from PySide2.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsItem
from PySide2 import QtCore
from Designs.de_sandbox import SandBox

def run_program():
    app_session = QApplication()  # Need to pass app_session to Main_window so it won't disappear

    scene = SandBox(app_session)

    scene.add_rect(1,2,3,4)
    scene.add_view()

    app_session.exec_()


if __name__ == '__main__':
    run_program()
