#!/usr/bin/python    

002 # tetris.py    

003 import sys    

004 import random    

005 from PyQt4 import QtCore, QtGui    

006 class Tetris(QtGui.QMainWindow):    

007     def __init__(self):    

008         QtGui.QMainWindow.__init__(self)    

009         self.setGeometry(300, 300, 180, 380)    

010         self.setWindowTitle('Tetris')    

011         self.tetrisboard = Board(self)    

012         self.setCentralWidget(self.tetrisboard)    

013         self.statusbar = self.statusBar()    

014         self.connect(self.tetrisboard, QtCore.SIGNAL("messageToStatusbar(QString)"),    

015             self.statusbar, QtCore.SLOT("showMessage(QString)"))    

016         self.tetrisboard.start()    

017         self.center()    

018     def center(self):    

019         screen = QtGui.QDesktopWidget().screenGeometry()    

020         size =  self.geometry()    

021         self.move((screen.width()-size.width())/2,    

022             (screen.height()-size.height())/2)    

023 class Board(QtGui.QFrame):    

024     BoardWidth = 10   

025     BoardHeight = 22   

026     Speed = 300   

027     def __init__(self, parent):    

028         QtGui.QFrame.__init__(self, parent)    

029         self.timer = QtCore.QBasicTimer()    

030         self.isWaitingAfterLine = False   

031         self.curPiece = Shape()    

032         self.nextPiece = Shape()    

033         self.curX = 0   

034         self.curY = 0   

035         self.numLinesRemoved = 0   

036         self.board = []    

037         self.setFocusPolicy(QtCore.Qt.StrongFocus)    

038         self.isStarted = False   

039         self.isPaused = False   

040         self.clearBoard()    

041         self.nextPiece.setRandomShape()    

042     def shapeAt(self, x, y):    

043         return self.board[(y * Board.BoardWidth) + x]    

044     def setShapeAt(self, x, y, shape):    

045         self.board[(y * Board.BoardWidth) + x] = shape    

046     def squareWidth(self):    

047         return self.contentsRect().width() / Board.BoardWidth    

048     def squareHeight(self):    

049         return self.contentsRect().height() / Board.BoardHeight    

050     def start(self):    

051         if self.isPaused:    

052             return   

053         self.isStarted = True   

054         self.isWaitingAfterLine = False   

055         self.numLinesRemoved = 0   

056         self.clearBoard()    

057         self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"),    

058             str(self.numLinesRemoved))    

059         self.newPiece()    

060         self.timer.start(Board.Speed, self)    

061     def pause(self):    

062         if not self.isStarted:    

063             return   

064         self.isPaused = not self.isPaused    

065         if self.isPaused:    

066             self.timer.stop()    

067             self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"), "paused")    

068         else:    

069             self.timer.start(Board.Speed, self)    

070             self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"),    

071                 str(self.numLinesRemoved))    

072         self.update()    

073     def paintEvent(self, event):    

074         painter = QtGui.QPainter(self)    

075         rect = self.contentsRect()    

076         boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()    

077         for i in range(Board.BoardHeight):    

078             for j in range(Board.BoardWidth):    

079                 shape = self.shapeAt(j, Board.BoardHeight - i - 1)    

080                 if shape != Tetrominoes.NoShape:    

081                     self.drawSquare(painter,    

082                         rect.left() + j * self.squareWidth(),    

083                         boardTop + i * self.squareHeight(), shape)    

084         if self.curPiece.shape() != Tetrominoes.NoShape:    

085             for i in range(4):    

086                 x = self.curX + self.curPiece.x(i)    

087                 y = self.curY - self.curPiece.y(i)    

088                 self.drawSquare(painter, rect.left() + x * self.squareWidth(),    

089                     boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),    

090                     self.curPiece.shape())    

091     def keyPressEvent(self, event):    

092         if not self.isStarted or self.curPiece.shape() == Tetrominoes.NoShape:    

093             QtGui.QWidget.keyPressEvent(self, event)    

094             return   

095         key = event.key()    

096         if key == QtCore.Qt.Key_P:    

097             self.pause()    

098             return   

099         if self.isPaused:    

100             return   

101         elif key == QtCore.Qt.Key_Left:    

102             self.tryMove(self.curPiece, self.curX - 1, self.curY)    

103         elif key == QtCore.Qt.Key_Right:    

104             self.tryMove(self.curPiece, self.curX + 1, self.curY)    

105         elif key == QtCore.Qt.Key_Down:    

106             self.tryMove(self.curPiece.rotatedRight(), self.curX, self.curY)    

107         elif key == QtCore.Qt.Key_Up:    

108             self.tryMove(self.curPiece.rotatedLeft(), self.curX, self.curY)    

109         elif key == QtCore.Qt.Key_Space:    

110             self.dropDown()    

111         elif key == QtCore.Qt.Key_D:    

112             self.oneLineDown()    

113         else:    

114             QtGui.QWidget.keyPressEvent(self, event)    

115     def timerEvent(self, event):    

116         if event.timerId() == self.timer.timerId():    

117             if self.isWaitingAfterLine:    

118                 self.isWaitingAfterLine = False   

119                 self.newPiece()    

120             else:    

121                 self.oneLineDown()    

122         else:    

123             QtGui.QFrame.timerEvent(self, event)    

124     def clearBoard(self):    

125         for i in range(Board.BoardHeight * Board.BoardWidth):    

126             self.board.append(Tetrominoes.NoShape)    

127     def dropDown(self):    

128         newY = self.curY    

129         while newY > 0:    

130             if not self.tryMove(self.curPiece, self.curX, newY - 1):    

131                 break   

132             newY -= 1   

133         self.pieceDropped()    

134     def oneLineDown(self):    

135         if not self.tryMove(self.curPiece, self.curX, self.curY - 1):    

136             self.pieceDropped()    

137     def pieceDropped(self):    

138         for i in range(4):    

139             x = self.curX + self.curPiece.x(i)    

140             y = self.curY - self.curPiece.y(i)    

141             self.setShapeAt(x, y, self.curPiece.shape())    

142         self.removeFullLines()    

143         if not self.isWaitingAfterLine:    

144             self.newPiece()    

145     def removeFullLines(self):    

146         numFullLines = 0   

147         rowsToRemove = []    

148         for i in range(Board.BoardHeight):    

149             n = 0   

150             for j in range(Board.BoardWidth):    

151                 if not self.shapeAt(j, i) == Tetrominoes.NoShape:    

152                     n = n + 1   

153             if n == 10:    

154                 rowsToRemove.append(i)    

155         rowsToRemove.reverse()    

156         for m in rowsToRemove:    

157             for k in range(m, Board.BoardHeight):    

158                 for l in range(Board.BoardWidth):    

159                     self.setShapeAt(l, k, self.shapeAt(l, k + 1))    

160         numFullLines = numFullLines + len(rowsToRemove)    

161         if numFullLines > 0:    

162             self.numLinesRemoved = self.numLinesRemoved + numFullLines    

163             self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"),    

164                 str(self.numLinesRemoved))    

165             self.isWaitingAfterLine = True   

166             self.curPiece.setShape(Tetrominoes.NoShape)    

167             self.update()    

168     def newPiece(self):    

169         self.curPiece = self.nextPiece    

170         self.nextPiece.setRandomShape()    

171         self.curX = Board.BoardWidth / 2 + 1   

172         self.curY = Board.BoardHeight - 1 + self.curPiece.minY()    

173         if not self.tryMove(self.curPiece, self.curX, self.curY):    

174             self.curPiece.setShape(Tetrominoes.NoShape)    

175             self.timer.stop()    

176             self.isStarted = False   

177             self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"), "Game over")    

178     def tryMove(self, newPiece, newX, newY):    

179         for i in range(4):    

180             x = newX + newPiece.x(i)    

181             y = newY - newPiece.y(i)    

182             if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:    

183                 return False   

184             if self.shapeAt(x, y) != Tetrominoes.NoShape:    

185                 return False   

186         self.curPiece = newPiece    

187         self.curX = newX    

188         self.curY = newY    

189         self.update()    

190         return True   

191     def drawSquare(self, painter, x, y, shape):    

192         colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,    

193                       0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]    

194         color = QtGui.QColor(colorTable[shape])    

195         painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,    

196             self.squareHeight() - 2, color)    

197         painter.setPen(color.light())    

198         painter.drawLine(x, y + self.squareHeight() - 1, x, y)    

199         painter.drawLine(x, y, x + self.squareWidth() - 1, y)    

200         painter.setPen(color.dark())    

201         painter.drawLine(x + 1, y + self.squareHeight() - 1,    

202             x + self.squareWidth() - 1, y + self.squareHeight() - 1)    

203         painter.drawLine(x + self.squareWidth() - 1,    

204             y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)    

205 class Tetrominoes(object):    

206     NoShape = 0   

207     ZShape = 1   

208     SShape = 2   

209     LineShape = 3   

210     TShape = 4   

211     SquareShape = 5   

212     LShape = 6   

213     MirroredLShape = 7   

214 class Shape(object):    

215     coordsTable = (    

216         ((0, 0),     (0, 0),     (0, 0),     (0, 0)),    

217         ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),    

218         ((0, -1),    (0, 0),     (1, 0),     (1, 1)),    

219         ((0, -1),    (0, 0),     (0, 1),     (0, 2)),    

220         ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),    

221         ((0, 0),     (1, 0),     (0, 1),     (1, 1)),    

222         ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),    

223         ((1, -1),    (0, -1),    (0, 0),     (0, 1))    

224     )    

225     def __init__(self):    

226         self.coords = [[0,0] for i in range(4)]    

227         self.pieceShape = Tetrominoes.NoShape    

228         self.setShape(Tetrominoes.NoShape)    

229     def shape(self):    

230         return self.pieceShape    

231     def setShape(self, shape):    

232         table = Shape.coordsTable[shape]    

233         for i in range(4):    

234             for j in range(2):    

235                 self.coords[i][j] = table[i][j]    

236         self.pieceShape = shape    

237     def setRandomShape(self):    

238         self.setShape(random.randint(1, 7))    

239     def x(self, index):    

240         return self.coords[index][0]    

241     def y(self, index):    

242         return self.coords[index][1]    

243     def setX(self, index, x):    

244         self.coords[index][0] = x    

245     def setY(self, index, y):    

246         self.coords[index][1] = y    

247     def minX(self):    

248         m = self.coords[0][0]    

249         for i in range(4):    

250             m = min(m, self.coords[i][0])    

251         return m    

252     def maxX(self):    

253         m = self.coords[0][0]    

254         for i in range(4):    

255             m = max(m, self.coords[i][0])    

256         return m    

257     def minY(self):    

258         m = self.coords[0][1]    

259         for i in range(4):    

260             m = min(m, self.coords[i][1])    

261         return m    

262     def maxY(self):    

263         m = self.coords[0][1]    

264         for i in range(4):    

265             m = max(m, self.coords[i][1])    

266         return m    

267     def rotatedLeft(self):    

268         if self.pieceShape == Tetrominoes.SquareShape:    

269             return self   

270         result = Shape()    

271         result.pieceShape = self.pieceShape    

272         for i in range(4):    

273             result.setX(i, self.y(i))    

274             result.setY(i, -self.x(i))    

275         return result    

276     def rotatedRight(self):    

277         if self.pieceShape == Tetrominoes.SquareShape:    

278             return self   

279         result = Shape()    

280         result.pieceShape = self.pieceShape    

281         for i in range(4):    

282             result.setX(i, -self.y(i))    

283             result.setY(i, self.x(i))    

284         return result    

285 app = QtGui.QApplication(sys.argv)    

286 tetris = Tetris()    

287 tetris.show()    

288 sys.exit(app.exec_()) 
