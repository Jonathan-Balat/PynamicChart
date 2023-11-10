from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem
from Designs.Objects.Rect_obj import RectObj


class SandBox(QGraphicsScene):

    def __init__(self, app_session):
        super().__init__()
        self.__app_session = app_session
    # NOTE: Overriding this breaks the passing of event to items. Learn how to reestablish this
    # def mousePressEvent(self, event):
    #     print(event.buttonDownScenePos(QtCore.Qt.MouseButton.LeftButton))  # Widget-screen position
    #     print(event.buttonDownScreenPos(QtCore.Qt.MouseButton.LeftButton))  # Absolute screen position

    def add_view(self):
        self.view = QGraphicsView(self)
        self.view.show()

    def add_rect(self, x, y, w, h):
        self.addItem(RectObj(self))
        # self.addRect(x, y, w, h)
        rect = self.items()[0]
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        ...
