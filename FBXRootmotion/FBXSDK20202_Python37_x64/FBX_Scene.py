
# @Author: anchen
# @Date:   2021-01-22 12:27:42
# @Last Modified by:   anchen
# @Last Modified time: 2021-01-25 20:17:58
import sys
#sys.path.append(r"D:\Git_Python\FBXRootmotion\gitee\FBXRootmotion\FBXSDK20202_Python37_x64")
import os
from FbxCommon import *

from fbx import *

class FBX_Class(object):

	def __init__(self, filename):
		"""
		FBX Scene Object
		"""
		self.filename = filename
		self.scene = None
		self.sdk_manager = None
		self.sdk_manager, self.scene = InitializeSdkObjects()
		LoadScene(self.sdk_manager, self.scene, filename)

		self.root_node = self.scene.GetRootNode()
		self.scene_nodes = self.get_scene_nodes()
		#globalSettings = self.scene.GetGlobalSettings()
		self.timeMode = self.scene.GetGlobalSettings().GetTimeMode()
		self.axis = self.scene.GetGlobalSettings().GetAxisSystem()
		self.max_axis = FbxAxisSystem(FbxAxisSystem.EPreDefinedAxisSystem(2))

		(targetName,extensionName) = os.path.splitext(os.path.basename(self.filename))

		self.targetName = targetName
		self.extensionName = extensionName

	def close(self):
		"""
		You need to run this to close the FBX scene safely
		"""
		# destroy objects created by the sdk
		self.sdk_manager.Destroy()

	def __get_scene_nodes_recursive(self, node):
		"""
		Rescursive method to get all scene nodes
		this should be private, called by get_scene_nodes()
		"""
		self.scene_nodes.append(node)
		for i in range(node.GetChildCount()):
			self.__get_scene_nodes_recursive(node.GetChild(i))

	def __cast_property_type(self, fbx_property):
		"""
		Cast a property to type to properly get the value
		"""
		casted_property = None

		unsupported_types = [fbx.eFbxUndefined, fbx.eFbxChar, fbx.eFbxUChar, fbx.eFbxShort, fbx.eFbxUShort, fbx.eFbxUInt,
							 fbx.eFbxLongLong, fbx.eFbxHalfFloat, fbx.eFbxDouble4x4, fbx.eFbxEnum, fbx.eFbxTime,
							 fbx.eFbxReference, fbx.eFbxBlob, fbx.eFbxDistance, fbx.eFbxDateTime, fbx.eFbxTypeCount]

		# property is not supported or mapped yet
		property_type = fbx_property.GetPropertyDataType().GetType()
		if property_type in unsupported_types:
			return None

		if property_type == fbx.eFbxBool:
			casted_property = fbx.FbxPropertyBool1( fbx_property )
		elif property_type == fbx.eFbxDouble:
			casted_property = fbx.FbxPropertyDouble1( fbx_property )
		elif property_type == fbx.eFbxDouble2:
			casted_property = fbx.FbxPropertyDouble2( fbx_property )
		elif property_type == fbx.eFbxDouble3:
			casted_property = fbx.FbxPropertyDouble3( fbx_property )
		elif property_type == fbx.eFbxDouble4:
			casted_property = fbx.FbxPropertyDouble4( fbx_property )
		elif property_type == fbx.eFbxInt:
			casted_property = fbx.FbxPropertyInteger1( fbx_property )
		elif property_type == fbx.eFbxFloat:
			casted_property = fbx.FbxPropertyFloat1( fbx_property )
		elif property_type == fbx.eFbxString:
			casted_property = fbx.FbxPropertyString( fbx_property )
		else:
			raise ValueError( 'Unknown property type: {0} {1}'.format(property.GetPropertyDataType().GetName(), property_type))

		return casted_property

	def get_scene_nodes(self):
		"""
		Get all nodes in the fbx scene
		"""
		self.scene_nodes = []
		for i in range(self.root_node.GetChildCount()):
			self.__get_scene_nodes_recursive(self.root_node.GetChild(i))
		return self.scene_nodes

	def get_type_nodes(self, type):
		"""
		Get nodes from the scene with the given type
		display_layer_nodes = fbx_file.get_type_nodes( u'DisplayLayer' )
		"""
		nodes = []
		num_objects = self.scene.RootProperty.GetSrcObjectCount()
		for i in range(0, num_objects):
			node = self.scene.RootProperty.GetSrcObject(i)
			if node:
				if node.GetTypeName() == type:
					nodes.append(node)
		return nodes

	def get_class_nodes(self, class_id):
		"""
		Get nodes in the scene with the given classid
		geometry_nodes = fbx_file.get_class_nodes( fbx.FbxGeometry.ClassId )
		"""
		nodes = []
		num_nodes = self.scene.RootProperty.GetSrcObjectCount(fbx.FbxCriteria.ObjectType(class_id))
		for index in range(0, num_objects):
			node = self.scene.RootProperty.GetSrcObject(fbx.FbxCriteria.ObjectType(class_id), index)
			if node:
				nodes.append(node)
		return nodes

	def get_property(self, node, property_string):
		"""
		Gets a property from an Fbx node
		export_property = fbx_file.get_property(node, 'no_export')
		"""
		fbx_property = node.FindProperty(property_string)
		return fbx_property

	def get_property_value(self, node, property_string):
		"""
		Gets the property value from an Fbx node
		property_value = fbx_file.get_property_value(node, 'no_export')
		"""
		fbx_property = node.FindProperty(property_string)
		if fbx_property.IsValid():
			# cast to correct property type so you can get
			casted_property = self.__cast_property_type(fbx_property)
			if casted_property:
				return casted_property.Get()
		return None

	def get_node_by_name(self, name):
		"""
		Get the fbx node by name
		"""
		self.get_scene_nodes()
		# right now this is only getting the first one found
		node = [ node for node in self.scene_nodes if node.GetName() == name ]
		if node:
			return node[0]
		return None

	def remove_namespace(self):
		"""
		Remove all namespaces from all nodes
		This is not an ideal method but
		"""
		self.get_scene_nodes()
		for node in self.scene_nodes:
			orig_name = node.GetName()
			split_by_colon = orig_name.split(':')
			if len(split_by_colon) > 1:
				new_name = split_by_colon[-1:][0]
				node.SetName(new_name)
		return True

	def remove_node_property(self, node, property_string):
		"""
		Remove a property from an Fbx node
		remove_property = fbx_file.remove_property(node, 'UDP3DSMAX')
		"""
		node_property = self.get_property(node, property_string)
		if node_property.IsValid():
			node_property.DestroyRecursively()
			return True
		return False

	def set_take_name(self):
		for i in range(self.scene.GetSrcObjectCount(FbxCriteria.ObjectType(FbxAnimStack.ClassId))):
			# Take 001 遍历 take
			lAnimStack = self.scene.GetSrcObject(FbxCriteria.ObjectType(FbxAnimStack.ClassId), i)
			if lAnimStack:
				lAnimStack.SetName(self.targetName)

	def get_anim_GetCurve(self,node,curve_type=1,curves_name="X"):

		#print("Node : %s" % node.GetName())
		KFCURVENODE_T_X = curves_name
		lAnimCurve = None

		for i in range(self.scene.GetSrcObjectCount(FbxCriteria.ObjectType(FbxAnimStack.ClassId))):
			# Take 001 遍历 take
			lAnimStack = self.scene.GetSrcObject(FbxCriteria.ObjectType(FbxAnimStack.ClassId), i)
			#print("Take: %s" % lAnimStack.GetName())
			nbAnimLayers = lAnimStack.GetSrcObjectCount(FbxCriteria.ObjectType(FbxAnimLayer.ClassId))
			#print("AnimLayers count: %s" % nbAnimLayers)

			#遍历动画层
			#for l in range(nbAnimLayers):
			#   lAnimLayer = lAnimStack.GetSrcObject(FbxCriteria.ObjectType(FbxAnimLayer.ClassId), l)
			#   print("AnimLayers name: %s" % lAnimLayer.GetName())

			lAnimLayer = lAnimStack.GetSrcObject(FbxCriteria.ObjectType(FbxAnimLayer.ClassId), 0)
			#print("AnimLayers name: %s" % lAnimLayer.GetName())
			if curve_type == 1:
				lAnimCurve = node.LclTranslation.GetCurve(lAnimLayer, KFCURVENODE_T_X)

			if curve_type == 2:
				lAnimCurve = node.LclRotation.GetCurve(lAnimLayer, KFCURVENODE_T_X)

			if curve_type == 3:
				lAnimCurve = node.LclScaling.GetCurve(lAnimLayer, KFCURVENODE_T_X)

		return lAnimCurve

	def remove_nodes_by_names(self, names):
		"""
		Remove nodes from the fbx file from a list of names
		names = ['object1','shape2','joint3']
		remove_nodes = fbx_file.remove_nodes_by_names(names)
		"""

		if names == None or len(names) == 0:
			return True

		self.get_scene_nodes()
		remove_nodes = [ node for node in self.scene_nodes if node.GetName() in names ]
		for node in remove_nodes:
			disconnect_node = self.scene.DisconnectSrcObject(node)
			remove_node = self.scene.RemoveNode(node)
		self.get_scene_nodes()
		return True
	def get_key_time(self,int_frames):
		time_num = FbxTime()
		time_num.SetTime( 0, 0, 0, int_frames, 0, self.timeMode)
		return time_num

	def set_rootmotion_anim(self,root_node_name,role_node_name,role_axis:"Y"):
		root_node = self.get_node_by_name(root_node_name)
		role_node = self.get_node_by_name(role_node_name)
		#3ds max 轴在 FBX 环境中
		# Y -> Z
		# Z -> Y
		if role_axis == "Y" :
			root_axis = "Z"
			filp_value = -1
		if role_axis == "Z" :
			root_axis = "Y"
			filp_value = -1

		if role_axis == "X":
			root_axis = "X"
			filp_value = 1

		if root_node and role_node:
			#print(root_node_name,role_node_name)
			role_node_y_AnimCurve = self.get_anim_GetCurve(role_node,1,role_axis)
			if not role_node_y_AnimCurve:
				return False

			root_node_y_AnimCurve = self.get_anim_GetCurve(root_node,1,root_axis)
			if not root_node_y_AnimCurve:
				return False


			role_KeyCount = role_node_y_AnimCurve.KeyGetCount()
			start_key_value = role_node_y_AnimCurve.KeyGetValue(0)
			#print("role_KeyCount ： %s" % role_KeyCount )

			role_node_y_AnimCurve.KeyModifyBegin()
			root_node_y_AnimCurve.KeyModifyBegin()

			for lCount in range(role_KeyCount):

				lKeyValue = role_node_y_AnimCurve.KeyGetValue(lCount)
				lKeyTime  = role_node_y_AnimCurve.KeyGetTime(lCount)
				new_value = lKeyValue - start_key_value
				role_node_y_AnimCurve.KeySetValue(lCount,start_key_value)

				lKeyIndex = root_node_y_AnimCurve.KeyAdd(lKeyTime)[0]

				root_node_y_AnimCurve.KeySetValue(lKeyIndex, new_value * filp_value)
				root_node_y_AnimCurve.KeySetInterpolation(lKeyIndex, FbxAnimCurveDef.eInterpolationCubic)

			role_node_y_AnimCurve.KeyModifyEnd()
			root_node_y_AnimCurve.KeyModifyEnd()
			return True
		else:
			print("root_node : %s  role_node : %s " %(root_node,role_node))
			return False
	def save(self, filename = None ):
		"""
		Save the current fbx scene as the incoming filename .fbx
		"""
		# save as a different filename
		if not filename is None:
			SaveScene(self.sdk_manager, self.scene, filename,pFileFormat=0)
		else:
			SaveScene(self.sdk_manager, self.scene, self.filename,pFileFormat=0)
		self.close()
	def save_as(self,filename = None):
		if not filename is None:
			filenameA = filename + "/"+ self.targetName + self.extensionName
			SaveScene(self.sdk_manager, self.scene, filenameA,pFileFormat=0)
		else:
			filenameB = os.path.dirname(self.filename) + "/"+ self.targetName +"_Rm"+ self.extensionName
			SaveScene(self.sdk_manager, self.scene, filenameB,pFileFormat=0)
		self.close()

"""
You will need to instantiate the class to access its methods
"""
if __name__ == '__main__':
	pass


	fbx_file_ = r"H:\Max_Project\UE4项目\测试资源\FBX\test\130.fbx"
	fbx_file_B = r"H:\Max_Project\UE4项目\测试资源\FBX\test\130_rm.FBX"
	fbx_file = FBX_Class(fbx_file_)

	#fbx_file.close()
	#node = fbx_file.get_node_by_name('Bip001')

	#fbx_file.get_anim_GetCurve(node)
	fbx_file.set_rootmotion_anim("Bone_root","Bip001","Y")
	fbx_file.save_as()
	#node_property = fbx_file.get_property(node, 'no_export')
	#node_property_value = fbx_file.get_property_value( node, 'no_export')
	#remove_property = fbx_file.remove_node_property(node, 'no_anim_export')
	#remove_property = fbx_file.remove_node_property(node, 'no_export')
	#remove_node = fbx_file.remove_nodes_by_names('hair_a_01')
