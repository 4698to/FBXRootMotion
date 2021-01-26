
import sys
from functools import partial
from distutils.util import strtobool

from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtWidgets import *
from PySide2 import QtUiTools
##20-20
#from PySide2 import shiboken2
##20-21
import qtmax
import pymxs
from pymxs import runtime as rt

import os

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QApplication.translate(context, text, disambig)


SCRIPT_LOC = os.path.split(__file__)[0]
sys.path.append(SCRIPT_LOC+"\\FBXSDK20202_Python37_x64")
#print(SCRIPT_LOC)
from FBX_Scene import FBX_Class

class FBXrootmontion_UI(QDialog):
	def __init__(self, parent=None):
		super(FBXrootmontion_UI, self).__init__(parent)
		self.resize(360, 381)

		self.setAcceptDrops(True)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
		#self.connect(self, QtCore.SIGNAL("dropped"), self.file_Dropped)

		self.groupBox_editname = QGroupBox(self)
		self.groupBox_editname.setGeometry(QtCore.QRect(5, 80, 350, 51))
		self.groupBox_editname.setObjectName(_fromUtf8("groupBox_editname"))

		self.lineEdit_rootname = QLineEdit(self.groupBox_editname)
		self.lineEdit_rootname.setText("root")
		self.lineEdit_rootname.setGeometry(QtCore.QRect(20, 20, 141, 21))
		#self.lineEdit_rootname.setGeometry(QtCore.QRect(192, 20, 141, 21))
		self.lineEdit_rootname.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.lineEdit_rootname.setAcceptDrops(False)
		self.lineEdit_rootname.setObjectName(_fromUtf8("lineEdit_rootname"))

		self.lineEdit_rolename =QLineEdit(self.groupBox_editname)
		self.lineEdit_rolename.setText("Bip001")
		#self.lineEdit_rolename.setGeometry(QtCore.QRect(20, 20, 141, 21))
		self.lineEdit_rolename.setGeometry(QtCore.QRect(192, 20, 141, 21))
		self.lineEdit_rolename.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.lineEdit_rolename.setAcceptDrops(False)
		self.lineEdit_rolename.setObjectName(_fromUtf8("lineEdit_rolename"))



		self.groupBox_timelen = QGroupBox(self)
		self.groupBox_timelen.setGeometry(QtCore.QRect(5, 130, 350, 101))
		self.groupBox_timelen.setObjectName(_fromUtf8("groupBox_timelen"))


		self.label_setsavepath = QLabel(self.groupBox_timelen)
		self.label_setsavepath.setGeometry(QtCore.QRect(20, 20, 72, 15))
		#self.label_setsavepath.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)

		self.label_dirpath = QLineEdit(self.groupBox_timelen)
		self.label_dirpath.setGeometry(QtCore.QRect(20, 40, 290, 21))
		self.label_dirpath.setReadOnly(True)
		self.get_dirpath = QPushButton(self.groupBox_timelen)
		self.get_dirpath.setGeometry(QtCore.QRect(312, 40, 21, 21))

		self.is_rename_take = QCheckBox(self.groupBox_timelen)
		self.is_rename_take.setGeometry(QtCore.QRect(20, 70, 300, 19))

		'''
		self.label_start = QLabel(self.groupBox_timelen)
		self.label_start.setGeometry(QtCore.QRect(20, 32, 72, 15))
		self.label_start.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
		self.label_start.setObjectName(_fromUtf8("label_start"))

		self.spinBox_start = QSpinBox(self.groupBox_timelen)
		self.spinBox_start.setGeometry(QtCore.QRect(100, 33, 101, 22))
		self.spinBox_start.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_start.setMaximum(99999)
		self.spinBox_start.setObjectName(_fromUtf8("spinBox_start"))
		self.Button_get_start = QPushButton(self.groupBox_timelen)
		self.Button_get_start.setGeometry(QtCore.QRect(220, 30, 111, 28))
		self.Button_get_start.setObjectName(_fromUtf8("Button_get_start"))
		self.spinBox_stop = QSpinBox(self.groupBox_timelen)
		self.spinBox_stop.setGeometry(QtCore.QRect(100, 63, 101, 22))
		self.spinBox_stop.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_stop.setMinimum(1)
		self.spinBox_stop.setMaximum(99999)
		self.spinBox_stop.setProperty("value", 1)
		self.spinBox_stop.setObjectName(_fromUtf8("spinBox_stop"))
		self.Button_get_stop = QPushButton(self.groupBox_timelen)
		self.Button_get_stop.setGeometry(QtCore.QRect(220, 60, 111, 28))
		self.Button_get_stop.setObjectName(_fromUtf8("Button_get_stop"))
		self.label_stop = QLabel(self.groupBox_timelen)
		self.label_stop.setGeometry(QtCore.QRect(20, 62, 72, 15))
		self.label_stop.setAlignment(QtCore.Qt.AlignCenter)
		self.label_stop.setObjectName(_fromUtf8("label_stop"))
		'''

		self.groupBox_pos = QGroupBox(self)
		self.groupBox_pos.setGeometry(QtCore.QRect(5, 230, 350, 101))
		self.groupBox_pos.setObjectName(_fromUtf8("groupBox_pos"))

		self.check_xyz_group = QButtonGroup(self)
		self.check_xyz_group.setExclusive(False)
		self.check_x = QCheckBox(self.groupBox_pos)
		self.check_x.setGeometry(QtCore.QRect(80, 20, 41, 19))
		self.check_x.setObjectName(_fromUtf8("check_x"))
		self.check_y =QCheckBox(self.groupBox_pos)
		self.check_y.setGeometry(QtCore.QRect(160, 20, 41, 19))
		self.check_y.setObjectName(_fromUtf8("check_y"))
		self.check_z = QCheckBox(self.groupBox_pos)
		self.check_z.setGeometry(QtCore.QRect(240, 20, 41, 19))
		self.check_z.setObjectName(_fromUtf8("check_z"))

		self.check_xyz_group.addButton(self.check_x,0)
		self.check_xyz_group.addButton(self.check_y,1)
		self.check_xyz_group.addButton(self.check_z,2)

		self.Button_do = QPushButton(self.groupBox_pos)
		self.Button_do.setGeometry(QtCore.QRect(20, 50, 311, 41))
		self.Button_do.setObjectName(_fromUtf8("Button_do"))

		self.groupBox_fbxfile = QGroupBox(self)
		self.groupBox_fbxfile.setGeometry(QtCore.QRect(5, 5, 350, 61))
		self.groupBox_fbxfile.setObjectName(_fromUtf8("groupBox_fbxfile"))

		self.label_filename = QLabel(self.groupBox_fbxfile)
		self.label_filename.setGeometry(QtCore.QRect(10, 20, 345, 30))
		self.label_filename.setAlignment(QtCore.Qt.AlignCenter)
		self.label_filename.setObjectName(_fromUtf8("label_stop"))

		self.progressBar = QProgressBar(self)
		self.progressBar.setEnabled(True)
		self.progressBar.setGeometry(QtCore.QRect(5, 340, 350, 16))
		self.progressBar.setProperty("value", 0)
		self.progressBar.setTextVisible(False)
		self.progressBar.setObjectName(_fromUtf8("progressBar"))
		self.label_help = QLabel(self)
		self.label_help.setGeometry(QtCore.QRect(150, 360, 71, 16))
		self.label_help.setAlignment(QtCore.Qt.AlignCenter)
		self.label_help.setObjectName(_fromUtf8("label_help"))
		self.label_help.setOpenExternalLinks(True)

		self.retranslateUi()
		self.show()

		self.links = []
		#QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self):
		self.setWindowTitle(_translate("self", "FBX Rootmotion 1.0", None))
		self.setWhatsThis(_translate("self", "FBX Rootmotion", None))
		self.groupBox_editname.setTitle(_translate("self", u"1：设置根骨骼和质心骨骼名字", None))


		self.groupBox_timelen.setTitle(_translate("self", u"2：其他设置", None))
		self.label_setsavepath.setText(u"保存目录：")
		self.is_rename_take.setText(u"以FBX文件名重命名 take 001 ")
		'''
		self.label_start.setText(_translate("self", u"起始帧：", None))
		self.Button_get_start.setText(_translate("self", u"设置", None))
		self.Button_get_stop.setText(_translate("self", u"设置", None))
		self.label_stop.setText(_translate("self", u"停止帧：", None))
		'''

		self.groupBox_pos.setTitle(_translate("self", u"3：位移", None))
		self.check_x.setText(_translate("self", "X", None))
		self.check_y.setText(_translate("self", "Y", None))
		self.check_z.setText(_translate("self", "Z", None))
		self.Button_do.setText(_translate("self", u"确定", None))
		self.groupBox_fbxfile.setTitle(_translate("self",u"0：FBX拖拽进这个范围内", None))
		self.label_filename.setText(".fbx")
		self.label_help.setText(u"<a href = 'https://gitee.com/to4698/ND_tools/tree/master/FBXRootmotion'>Help</a>")


		#self.Button_get_start.clicked.connect(self.get_start_time)
		#self.Button_get_stop.clicked.connect(self.get_stop_time)
		self.get_dirpath.clicked.connect(self.get_save_path)

		self.Button_do.clicked.connect(self.apply_rootmotion)
	def get_save_path(self):
		temp_dir = None
		if len(self.links) >0:
			temp_dir = os.path.dirname(self.links[0])

		dir_path = QFileDialog.getExistingDirectory(self,u"选择保存文件夹",temp_dir)
		if len(dir_path) > 1 :
			self.label_dirpath.setText(dir_path)
	def get_start_time(self):
		self.spinBox_start.setValue(rt.sliderTime.frame)
	def get_stop_time(self):
		self.spinBox_stop.setValue(rt.sliderTime.frame)
	def apply_rootmotion(self):
		if len(self.links) > 0 :
			if len(self.lineEdit_rootname.text()) > 0 and len(self.lineEdit_rolename.text()) > 0 :
				#设置根运动
				if self.check_xyz_group.checkedId() >= 0 :
					for index,file in enumerate(self.links):
						fbx_mod = FBX_Class(file)
						print("%s" % file)
						if self.check_y.isChecked():
							print("-> YY")
							is_ok = fbx_mod.set_rootmotion_anim(self.lineEdit_rootname.text(),self.lineEdit_rolename.text(),"Y")
							if not is_ok:
								print("Y -> back-out")
						if self.check_z.isChecked():
							print("-> ZZ")
							is_ok = fbx_mod.set_rootmotion_anim(self.lineEdit_rootname.text(),self.lineEdit_rolename.text(),"Z")
							if not is_ok:
								print("Z -> back-out")
						if self.check_x.isChecked():
							print("-> XX")
							is_ok = fbx_mod.set_rootmotion_anim(self.lineEdit_rootname.text(),self.lineEdit_rolename.text(),"X")
							if not is_ok:
								print("X -> back-out")

						if self.is_rename_take.isChecked():
							fbx_mod.set_take_name()
						fbx_mod.save_as(self.label_dirpath.text())
						print("done!")
						self.progressBar.setValue((index + 1) / len(self.links) * 100)
				else:
				#不设置根运动，只重命名take
					if self.is_rename_take.isChecked():
						for index,file in enumerate(self.links):
							fbx_mod = FBX_Class(file)
							print("%s" % file)
							fbx_mod.set_take_name()
							fbx_mod.save_as(self.label_dirpath.text())
							print("done!")
							self.progressBar.setValue((index + 1) / len(self.links) * 100)

	def file_Dropped(self,lists):
		file_len = len(lists)
		if file_len > 0 :
			self.Button_do.setText(u" -> %s 份文件！ " % file_len)
			self.progressBar.setValue(0)
			self.label_filename.setText(os.path.basename(lists[0]) + "\n"+(os.path.dirname(lists[0])))
			self.label_dirpath.setText(os.path.dirname(lists[0]))
	# 文件拖拽
	def dragEnterEvent(self, event):

		if event.mimeData().hasUrls:
			event.accept()
		else:
			event.ignore()


	def dragMoveEvent(self, event):

		if event.mimeData().hasUrls:
			event.setDropAction(QtCore.Qt.CopyAction)
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):

		if event.mimeData().hasUrls:
			event.setDropAction(QtCore.Qt.CopyAction)
			event.accept()
			self.links = []
			for url in event.mimeData().urls():

				self.links.append(str(url.toLocalFile()))
			#self.emit(QtCore.SIGNAL("dropped"), links)
			self.file_Dropped(self.links)
		else:
			event.ignore()

if __name__ == "__main__":

	main_window = QtWidgets.QWidget.find(rt.windows.getMAXHWND())
	FBXrootmontion_UI(parent=main_window)

