from PySide2.QtWidgets import QGraphicsTextItem, QGraphicsItem, QGraphicsRectItem
from PySide2.QtCore import QRectF


class RectObj(QGraphicsTextItem):

    def __init__(self, parent, x, y, w, h, penWidth=3):
        super().__init__()
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.setParent(parent)
        self.setPlainText("100")

        self.__penWidth = penWidth
        self.__bound = QRectF(x - (self.__penWidth / 2), y - (self.__penWidth / 2), w + self.__penWidth, h + self.__penWidth)
        self.__textbound = QRectF(x, y, w, h)
        self.__geom = (x,y,w,h)

    def boundingRect(self):
        x,y,w,h = self.__geom
        self.__bound = QRectF(x - (self.__penWidth / 2), y - (self.__penWidth / 2), w + self.__penWidth, h + self.__penWidth)

        return self.__bound

    def paint(self, painter, option, widget):
        painter.drawText(self.__geom[0], self.__geom[1], "BOX")
        painter.drawRoundedRect(self.__bound, 5, 5)
        # painter.drawRoundedRect(0, 0, 20, 20, 5, 5)

    # def mouseDoubleClickEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.setPlainText("left mouse")
    #         print("left mouse")
    #         # TODO: Add text filling here
    #
    #     if event.button() == Qt.RightButton:
    #         self.setPlainText("right mouse")
    #         print("right mouse")
