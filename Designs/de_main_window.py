from PySide2.QtWidgets import QMainWindow, QWidget, QStackedLayout


class MainWindow(QMainWindow):

    def __init__(self, app_sess):
        super().__init__()
        self.__app_session = app_sess

        # STEP 1: Check current monitor in use, get size and run window with adequate size there
        self.setObjectName("MainWindow")
        self.setWindowTitle("PynamicChart")

        desk = self.__app_session.primaryScreen()
        _, _, width, height = desk.availableGeometry().getCoords()

        window_sq_factor = 0.75

        x, y = width * (1 - window_sq_factor), height * (1 - window_sq_factor)
        self.setFixedSize(width * window_sq_factor, height * window_sq_factor)
        self.move(x / 2, y / 2)

        # STEP 2: Create panel on left, and right size GraphicsView
        self.__setup_ui()

    def __setup_ui(self):
        self.wd_central = QWidget(self)
        self.wd_central.setFixedSize(self.width(), self.height())
        self.wd_central.setStyleSheet("QWidget {background-color: rgba(100,100,100,255);}")

        # # REPLACE WITH PANEL CLASS
        self.wd_panel = QWidget(self.wd_central)
        self.wd_panel.setFixedSize(self.wd_central.width()*0.15, self.wd_central.height())
        self.wd_panel.setStyleSheet("QWidget {background-color: rgba(255,100,100,255);}")

        # REPLACE WITH SANDBOX CLASS
        self.wd_sandbox = QWidget(self.wd_central)
        self.wd_sandbox.setFixedSize(self.wd_central.width() - self.wd_panel.width(), self.wd_central.height())
        self.wd_sandbox.setStyleSheet("QWidget {background-color: rgba(100,100,255,255);}")
        self.wd_sandbox.move(self.wd_panel.width(), 0)

        self.ly_sandbox = QStackedLayout(self.wd_sandbox)

        # REF: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QToolBar.html#qtoolbar
        # self.t_bar = QToolBar()
        # self.t_bar.addAction("THIS")
        # self.t_bar.show()
        # self.addToolBar(Qt.TopToolBarArea, self.t_bar)

    def setSandbox(self, widget):
        self.sandbox = widget
        self.ly_sandbox.addWidget(self.sandbox.view)

    def setPanel(self, widget):
        self.panel = widget


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication

    app_session = QApplication()

    mw = MainWindow(app_session)
    mw.show()

    app_session.exec_()
