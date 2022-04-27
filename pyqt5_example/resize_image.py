def resizeImageWithQT(src, dest):
    pixmap = QtGui.QPixmap(src)
    pixmap_resized = pixmap.scaled(720, 405, QtCore.Qt.KeepAspectRatio)
    if not os.path.exists(os.path.dirname(dest)): os.makedirs(os.path.dirname(dest))
    pixmap_resized.save(dest)