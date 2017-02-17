#!/usr/bin/env python
# coding: utf-8

import sys
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  

reload(sys)
sys.setdefaultencoding('utf-8')
  
class SinglePageRenderer(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
   
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()
#     sys.exit(app.exec_())

#TEST STUB    
# url = 'http://www.vrapce.mk/'  
# r = SinglePageRenderer(url)  
# html = r.frame.toHtml()
# print html
