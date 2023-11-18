from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem
# from Designs.Objects.Rect_obj import RectObj
from Designs.Objects.RectObj2 import RectObj


class SandBox(QGraphicsScene):

    def __init__(self, parent):
        super().__init__(parent)
    # NOTE: Overriding this breaks the passing of event to items. Learn how to reestablish this
    # def mousePressEvent(self, event):
    #     print(event.buttonDownScenePos(QtCore.Qt.MouseButton.LeftButton))  # Widget-screen position
    #     print(event.buttonDownScreenPos(QtCore.Qt.MouseButton.LeftButton))  # Absolute screen position
        self.add_view()

    def add_view(self):
        self.view = QGraphicsView(self)
        self.view.show()

    def add_rect(self, x, y, w, h):
        self.addItem(RectObj(self, x, y, w, h))
        # rect = self.items()[0]
        # rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
