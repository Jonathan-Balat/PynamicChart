from PySide2.QtWidgets import QGraphicsScene, QGraphicsView
from Designs.Objects.Obj_Rect import RectObj


class SandBox(QGraphicsScene):

    def __init__(self, parent):
        super().__init__(parent)
        self.view = QGraphicsView(self)
        self.view.show()
    # NOTE: Overriding this breaks the passing of event to items. Learn how to reestablish this
    # def mousePressEvent(self, event):
    #     print(event.buttonDownScenePos(QtCore.Qt.MouseButton.LeftButton))  # Widget-screen position
    #     print(event.buttonDownScreenPos(QtCore.Qt.MouseButton.LeftButton))  # Absolute screen position

    def add_rect(self, x, y, w, h):
        self.addItem(RectObj(self, x, y, w, h))
