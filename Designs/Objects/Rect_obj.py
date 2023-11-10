from PySide2.QtWidgets import QGraphicsItem, QGraphicsRectItem
from PySide2.QtCore import QRectF


class RectObj(QGraphicsItem):

    def __init__(self, parent):
        super().__init__()

    def boundingRect(self):
        penWidth = 1.0
        return QRectF(-10 - penWidth / 2, -10 - penWidth / 2,
                      20 + penWidth, 20 + penWidth)

    def paint(self, painter, option, widget):
        painter.drawRoundedRect(-10, -10, 20, 20, 5, 5)

    def setWidth(self, newWidth):
        width = 0
        if width != newWidth:
            self.prepareGeometryChange()
            width = newWidth
