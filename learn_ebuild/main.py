import inspect
from functools import cache
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QListView, QButtonGroup, QRadioButton
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition
import sys
import os
import enum
import json
import _thread
import time
from main_window import Ui_mainWindow


class LanguageType(enum.Enum):
    CN = 0
    EN = 1


LanguageQms = {LanguageType.CN.value: 'language/cn.qm',
               LanguageType.EN.value: 'language/en.qm'}

json_config_path = './config.json'
ini_config_path = './config.ini'


class ListThread(QThread):
    tirgger = pyqtSignal(str)

    def __init__(self, parent):
        QThread.__init__(self, parent)
        self.working = True
        self.idx = 0
        self.mutex = QMutex()
        self.condition = QWaitCondition()
        self.paused = False
        self.stop_flag = False

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while not self.stop_flag:
            self.mutex.lock()
            if self.paused:
                self.condition.wait(self.mutex)
            self.mutex.unlock()

            self.tirgger.emit(str(self.idx))
            self.idx += 1
            time.sleep(1)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False
        self.condition.wakeAll()

    def stop(self):
        self.stop_flag = True


class SetupMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.win = Ui_mainWindow()
        self.win.setupUi(self)

        self.win.actionSave.triggered.connect(self.save_json_config)
        self.win.actionOpen.triggered.connect(self.open_file)
        self.win.openLangFolderBtn.clicked.connect(self.open_lang_folder)
        self.win.openLangFolderSelectBtn.clicked.connect(
            self.open_lang_folder_select)

        self.update_thread_btns()
        self.win.startBtn.clicked.connect(self.start_thread)
        self.win.pauseBtn.clicked.connect(self.pause_thread)
        self.win.resumeBtn.clicked.connect(self.resume_thread)
        self.win.stopBtn.clicked.connect(self.stop_thread)

        self.init_language()
        self.load_json_config()
        self.update_ui()

    def add_list_item(self, text):
        self.win.listWidget.addItem(text)

    def update_thread_btns(self):
        self.win.startBtn.setEnabled(self.list_thread == None)
        self.win.stopBtn.setEnabled(self.list_thread != None)
        self.win.resumeBtn.setEnabled(
            self.list_thread != None and self.list_thread.paused)
        self.win.pauseBtn.setEnabled(
            self.list_thread != None and not self.list_thread.paused)

    def start_thread(self):
        self.list_thread = ListThread(self)
        self.list_thread.tirgger.connect(self.add_list_item)

        self.list_thread.start()
        self.update_thread_btns()

    def pause_thread(self):
        self.list_thread.pause()
        self.update_thread_btns()

    def resume_thread(self):
        self.list_thread.resume()
        self.update_thread_btns()

    def stop_thread(self):
        self.list_thread.stop()
        self.list_thread = None
        self.update_thread_btns()

    def open_lang_folder(self):
        def start_explorer(path):
            time.sleep(2)
            os.system(f"explorer {path}")

        path = os.path.join(os.getcwd(), 'language')
        _thread.start_new_thread(start_explorer, (path,))

    def open_lang_folder_select(self):
        path = os.path.join(os.getcwd(), 'language', 'cn.qm')
        os.system(f"explorer /select,{path}")

    def update_json_config(self):
        self.config['language'] = self.languageGroup.checkedId()

    def update_ui(self):
        language = self.config.get('language', 0)
        print(language)
        self.languageGroup.buttons()[language].setChecked(True)

    def load_json_config(self):
        if not os.path.exists(json_config_path):
            self.config = {
                'language': LanguageType.CN.value,
            }
            return
        with open(json_config_path, 'r') as f:
            self.config = json.load(f)

    def save_json_config(self):
        self.update_json_config()
        with open(json_config_path, 'w') as f:
            json.dump(self.config, f)

    def init_language(self):
        self.translator = QtCore.QTranslator()
        self.languageGroup = QButtonGroup()
        self.languageGroup.addButton(
            self.win.cnRadioButton, LanguageType.CN.value)
        self.languageGroup.addButton(
            self.win.enRadioButton, LanguageType.EN.value)
        self.languageGroup.setExclusive(True)
        self.languageGroup.buttonToggled.connect(self.change_language)

    def change_language(self, btn: QRadioButton):
        if not btn.isChecked():
            return
        qm_path = LanguageQms.get(self.languageGroup.id(btn), 'cn.qm')
        self.translator.load(qm_path)
        QtCore.QCoreApplication.installTranslator(self.translator)
        self.win.retranslateUi(self)

    def open_file(self):
        self.statusbar.showMessage('open file')
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹")


class UIControll(object):
    def __init__(self):
        app = QApplication(sys.argv)
        self.config_root_path = os.getcwd()

        # 创建主窗口
        self.main_window = SetupMainWindow()
        # 显示主窗口
        self.main_window.show()

        # 进入程序主循环
        sys.exit(app.exec_())


@cache
def test(a, b, c=1):
    return a + b + c


if __name__ == "__main__":
    UIControll()
