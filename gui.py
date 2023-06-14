import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 그래픽 섹션에 그릴 객체들의 base class.
class DrawObject():
    def __init__(self, texture_path1, texture_path2, global_scene, width=10, height=10):
        self.texture1 = QImage()
        self.texture2 = QImage()
        self.texture_flag = 0
        self.brush = QBrush()
        self.rect = QGraphicsRectItem(0, 0, width, height)
        self.width = width
        self.height = height

        self.last_mouse_pos = QPoint()

        self.initialize_texture(texture_path1, texture_path2, global_scene)

    def initialize_texture(self, texture_path1, texture_path2, global_scene):
        self.texture1.load(texture_path1)
        if texture_path2 != '':
            self.texture2.load(texture_path2)

        self.brush.setTextureImage(self.texture1)
        self.rect.setBrush(self.brush)
        self.rect.setPen(QPen(Qt.NoPen))

        global_scene.addItem(self.rect)

    def update_texture(self, global_scene):
        if self.texture2.isNull():
            return

        if self.texture_flag == 0:
            global_scene.removeItem(self.rect)

            self.texture_flag = 1
            self.brush.setTextureImage(self.texture2)
            self.rect.setBrush(self.brush)
            self.rect.setPen(QPen(Qt.NoPen))

            global_scene.addItem(self.rect)

        elif self.texture_flag == 1:
            global_scene.removeItem(self.rect)

            self.texture_flag = 0
            self.brush.setTextureImage(self.texture1)
            self.rect.setBrush(self.brush)
            self.rect.setPen(QPen(Qt.NoPen))

            global_scene.addItem(self.rect)

# 아두이노 보드 클래스.
class Board(DrawObject):
    def __init__(self, texture_path1, texture_path2, global_scene, width=10, height=10):
        super().__init__(texture_path1, texture_path2, global_scene, width, height)
        self.type = "BOARD"

        ## 추후 추가 기능 ##
        # ddrx, portx, pinx는 아두이노 보드가 가지고 있는 설정 핀 값 전체를 가짐.
        # ddrx, portx, poinx는 딕셔너리  ex. {'A10': 1} ==> A타입 10번째 값이 1임
        # self.ddrx = {}
        # self.portx = {}
        # self.pinx = {}

        self.pin_rect = QGraphicsEllipseItem(184, 7, 4, 4)
        self.power_rect = QGraphicsEllipseItem(139, 177, 4, 4)
        self.power_rect2 = QGraphicsEllipseItem(112, 177, 4, 4)
        self.pin_rect.setPen(QPen(QColor(255, 0, 0)))
        self.power_rect.setPen(QPen(QColor(255, 0, 0)))
        self.power_rect2.setPen(QPen(QColor(255, 0, 0)))

        self.lines = []
        
        global_scene.addItem(self.pin_rect)
        global_scene.addItem(self.power_rect)
        global_scene.addItem(self.power_rect2)

    ## 추후 추가 기능 ##
    # ddrx, portx, pinx는 무조건 하나의 키-데이터를 받음. 만약 변경값이 없으면 값을 -1로 채울것.
    def set_pio(self, ddrx, portx, pinx):
        new_key = ddrx.keys()[0]
        if new_key in self.ddrx:
            print("already have key.")
            return
        
        if ddrx[new_key] != -1:
            self.ddrx[new_key] = ddrx[new_key]
        if portx[new_key] != -1:
            self.portx[new_key] = portx[new_key]
        if pinx[new_key] != -1:
            self.pinx[new_key] = pinx[new_key]

    def add_line(self, lines, is_point):
        for line in lines:
            self.lines.append(line)
        self.is_point = is_point

    def add_line(self, lines, is_point):
        for line in lines:
            self.lines.append(line)
            self.is_point = is_point


    ## 추후 추가 기능 ## 
    def udpate(self, ddrx, portx, pinx):
        # ddrx, portx, poinx는 딕셔너리  ex. {'A10': 1} ==> A타입 10번째 값이 1임
        key = ddrx.keys()[0]
        self.update_flag = False
        if key in self.ddrx and self.ddrx[key] == ddrx[key]:
            
            if self.portx[key] != portx[key]:
                self.portx[key] = portx[key]
                self.update_flag = True

            if pinx[key] != pinx[key]:
                self.pinx[key] = pinx[key]
                self.update_flag = True

        return self.update_flag
    
    def set_position(self, x, y):
        self.rect.setPos(QPoint(x, y))
        self.pin_rect.setPos(QPoint(x, y))
        self.power_rect.setPos(QPoint(x, y))
        self.power_rect2.setPos(QPoint(x, y))
            
# LED 모듈 클래스
class LED(DrawObject):
    def __init__(self, texture_path1, texture_path2, global_scene, width=10, height=10):
        super().__init__(texture_path1, texture_path2, global_scene, width, height)
        self.type = "LED"
        
        ## 추후 추가 기능 ##
        # ddrx, portx, pinx는 아두이노 보드에 연결된 핀의 정보만을 가짐
        # ddrx, portx, poinx는 딕셔너리  ex. {'A10': 1} ==> A타입 10번째 값이 1임
        # self.ddrx = {}
        # self.portx = {}
        # self.pinx = {}

        self.power_plus = QGraphicsEllipseItem(389, 44, 4, 4)
        self.power_minus = QGraphicsEllipseItem(418, 44, 4, 4)
        self.led1_pin = QGraphicsEllipseItem(348, 353, 4, 4)

        self.power_plus.setPen(QPen(QColor(255, 0, 0)))
        self.power_minus.setPen(QPen(QColor(255, 0, 0)))
        self.led1_pin.setPen(QPen(QColor(255, 0, 0)))

        self.lines = []

        global_scene.addItem(self.power_plus)
        global_scene.addItem(self.power_minus)
        global_scene.addItem(self.led1_pin)

    def add_line(self, lines, is_point):
        for line in lines:
            self.lines.append(line)
        self.is_point = is_point

    ## 추후 추가 기능 ##
    def update(self, ddrx, portx, pinx):
        # ddrx, portx, poinx는 딕셔너리  ex. {'A10': 1} ==> A타입 10번째 값이 1임
        key = ddrx.keys()[0]
        self.update_flag = False
        if key in self.ddrx and self.ddrx[key] == ddrx[key]:
            
            if self.portx[key] != portx[key]:
                self.portx[key] = portx[key]
                self.update_flag = True

            if pinx[key] != pinx[key]:
                self.pinx[key] = pinx[key]
                self.update_flag = True

        return self.update_flag
    
    def set_position(self, x, y):
        self.rect.setPos(QPoint(x, y))
        self.power_plus.setPos(QPoint(x, y))
        self.power_minus.setPos(QPoint(x, y))
        self.led1_pin.setPos(QPoint(x, y))

# 전선 클래스
class Wire():
    def __init__(self, left_object, right_object, global_scene):
        self.type = "WIRE"
        self.left_point = left_object
        self.right_point = right_object

        x1 = left_object.x() + left_object.rect().x()
        y1 = left_object.y() + left_object.rect().y()
        x2 = right_object.x() + right_object.rect().x()
        y2 = right_object.y() + right_object.rect().y()

        self.line = QGraphicsLineItem(QLineF(x1, y1, x2, y2))

        global_scene.addItem(self.line)

    def set_color(self):
        self.line.setPen(QPen(QColor(255, 0, 0)))

    def update_scene(self, global_scene):
        global_scene.removeItem(self.line)
        global_scene.addItem(self.line)

form_window = uic.loadUiType("main_program.ui")[0]

class ArduinoGui(QMainWindow, form_window):
    def __init__(self):
        # 인터페이스 컴포넌트 초기화
        super().__init__()
        self.setupUi(self)
        self.AddComponent.clicked.connect(self.AddComponentInBoard)
        self.Stop.clicked.connect(self.StopExecuting)
        self.Execute.clicked.connect(self.ExecuteCode)
        self.UserCodeSection

        # 소스코드 섹션 파일 읽고 섹션 초기화.
        source_file = open("source/user.c", "r", encoding="UTF8")
        source_data = ''
        while True:
            line = source_file.readline()
            if not line:
                break
            source_data += line
        self.UserCodeSection.setText(source_data)

        # 그래픽 섹션 렌더링을 위한 초기 변수.
        self.scene = QGraphicsScene()
        self.drawing_item = []
        self.signal = None
        self.loop_signal = False

        # 각 컴포넌트 초기화.
        board = Board(texture_path1="gui_build_image/Arduino_DUE_V02b_breadboard.png", texture_path2='', width=336, height=189, global_scene=self.scene)
        led = LED(texture_path1="gui_build_image/LED_MODULE.png", texture_path2="gui_build_image/LED_MODULE_ON.png", width=465, height=405, global_scene=self.scene)
        board.set_position(0, 500)
        led.set_position(100, 0)

        wire1 = Wire(board.power_rect, led.power_plus, self.scene)
        wire2 = Wire(board.power_rect2, led.power_minus, self.scene)
        wire3 = Wire(board.pin_rect, led.led1_pin, self.scene)
        wireSet = [wire1, wire2, wire3]
        wire2.set_color()
        board.add_line(wireSet, True)
        led.add_line(wireSet, False)

        # 현재 장면에 컴포넌트 추가함.
        self.drawing_item.append(board)
        self.drawing_item.append(led)
        self.drawing_item.append(wire1)
        self.drawing_item.append(wire2)
        self.drawing_item.append(wire3)

        # 그래픽 섹션에 장면 렌더링.
        self.ArduinoPlane.setScene(self.scene)

    def write_source_code(self, data):
        print('data write complete')
        print(data)

    ## 추후 추가 기능 ##
    def AddComponentInBoard(self):
        print('click add button')

    # 실행 버튼 시 동작
    def ExecuteCode(self):
        print('click execute button')

        ## debug section ##
        source_code = self.UserCodeSection.toPlainText()
        self.write_source_code(source_code)
        #####################

        ## debug section ## 
        self.loop_signal = True
        flag = False
        divisor = None
        i = 0
        j = 0
        #####################

        while self.loop_signal:
            ## debug section ## 
            i += 1
            if i > 1000000:
                i = 0

            divisor = i // 500
            if i % 500 == 0 and divisor % 500 == 1:
                flag = False
                continue
            if divisor % 2 == 1:
                continue


            if flag == True:
                continue
            flag = True
            #####################

            ## 추가 부분.
            # self.signal 값에 0, 1이 들어감.
            # sleep을 넣으려고 했지만, 스레드 구조를 어떻게 짜야할지 애매해서 포기.
            # 이미 에뮬레이션 단계에서 1초 sleep이 된다고 가정하고 값을 그대로 반영.
            # 구현 시, prev_signal 변수에 이전 값을 저장하고,
            # 새로 값을 받아왔을 때, 이전 변수와 다르면 새로 렌더링함.


            # 업데이트 변수에 따른 렌더링 부분.
            for item in self.drawing_item:
                if item.type != "WIRE":
                    item.update_texture(self.scene)
                else:
                    item.update_scene(self.scene)
            QApplication.processEvents()

    # 정지 버튼 시 동작
    def StopExecuting(self):
        if self.loop_signal == True:
            self.loop_signal = False

    # 메인 윈도우 종료 시 동작
    def closeEvent(self, event):
        self.StopExecuting()


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    main_window = ArduinoGui()
    main_window.show()
    sys.exit(app.exec_())
