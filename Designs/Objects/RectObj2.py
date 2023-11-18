from PySide2.QtWidgets import QGraphicsTextItem, QGraphicsItem, QGraphicsRectItem, QGraphicsSimpleTextItem
from PySide2.QtCore import QRectF, Qt, QRect


class RectObj(QGraphicsItem):

    def __init__(self, parent, x, y, w, h, penWidth=3):
        super().__init__()
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)

        # ref: https://stackoverflow.com/questions/59174317/how-to-add-text-inside-qgraphicspolygonitem-while-using-qpolygonf-for-drawing
        self.__textItem = QGraphicsSimpleTextItem("Text here", self)
        self.__textItem.shape()

        self.__penWidth = penWidth

        self.__bound = None
        self.__geom = (x, y, w, h)

    def boundingRect(self):
        return QRect(self.__geom[0], self.__geom[1], self.__geom[2], self.__geom[3])

    def paint(self, painter, option, widget):
        painter.drawRoundedRect(self.__geom[0], self.__geom[1], self.__geom[2], self.__geom[3], 2, 2)

    # def mouseDoubleClickEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.setPlainText("left mouse")
    #         print("left mouse")
    #         # TODO: Add text filling here
    #
    #     if event.button() == Qt.RightButton:
    #         self.setPlainText("right mouse")
    #         print("right mouse")
